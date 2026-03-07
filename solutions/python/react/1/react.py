class Cell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._dependents = set()

    def add_dependent(self, cell):
        self._dependents.add(cell)

    def notify_dependents(self, changed):
        for cell in self._dependents:
            cell.recompute(changed)

    @property
    def value(self):
        return self._value


class InputCell(Cell):

    @Cell.value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value

            changed = {}
            self.notify_dependents(changed)

            for cell, old_value in changed.items():
                if cell.value != old_value:
                    cell.call_callbacks()


class ComputeCell(Cell):

    def __init__(self, inputs, compute_function):
        self._inputs = inputs
        self._compute_function = compute_function
        self._callbacks = set()

        for cell in inputs:
            cell.add_dependent(self)

        super().__init__(self._compute())

    def _compute(self):
        return self._compute_function([cell.value for cell in self._inputs])

    def recompute(self, changed):
        new_value = self._compute()

        if new_value != self._value:
            changed.setdefault(self, self._value)
            self._value = new_value
            self.notify_dependents(changed)

    def add_callback(self, callback):
        self._callbacks.add(callback)

    def remove_callback(self, callback):
        self._callbacks.discard(callback)

    def call_callbacks(self):
        for callback in self._callbacks:
            callback(self._value)
