section .text
global steps

steps:
    xor rax, rax            ; Clear rax (step counter)
    mov rbx, rdi            ; Move input n from rdi to rbx
    
    cmp rbx, 1              ; If n == 1, return 0
    je .end
    cmp ebx, 0              ; Check lower 32 bits for <= 0
    jle .fail               ; Jump if n <= 0 (zero or negative)

.loop:
    cmp rbx, 1              ; If n == 1, done
    je .end
    inc rax                 ; Increment step counter
    test rbx, 1             ; Check if n is odd or even
    jz .even
.odd:
    mov rdx, rbx            ; Save n to rdx
    shl rbx, 1              ; rbx = 2n
    add rbx, rdx            ; rbx = 3n
    inc rbx                 ; rbx = 3n + 1
    jmp .loop
.even:
    shr rbx, 1              ; n = n / 2
    jmp .loop
.end:
    ret                     ; Return step count in rax
.fail:
    mov rax, -1             ; Return -1 for invalid input
    ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
