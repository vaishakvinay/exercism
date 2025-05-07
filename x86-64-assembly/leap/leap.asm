section .text
global leap_year
leap_year:
   ; Input: rdi = year
    ; Output: rax = 1 (leap year) or 0 (not a leap year)

    xor rax, rax         ; Default return value = 0 (not a leap year)

    ; Check if year is divisible by 4 (year % 4 == 0)
    mov rdx, 0
    mov rax, rdi
    mov rcx, 4
    div rcx
    test rdx, rdx        ; If remainder != 0, it's NOT a leap year
    jnz .not_leap_year
; Check if year is divisible by 100 (year % 100 == 0)
    mov rax, rdi
    mov rcx, 100
    div rcx
    test rdx, rdx
    jnz .leap_year       ; If remainder != 0, it's a leap year

    ; Check if year is divisible by 400 (year % 400 == 0)
    mov rax, rdi
    mov rcx, 400
    div rcx
    test rdx, rdx
    jz .leap_year        ; If remainder == 0, it's a leap year

.not_leap_year:
    xor rax, rax         ; Return 0 (not a leap year)
    ret

.leap_year:
    mov rax, 1           ; Return 1 (leap year)
    ret


%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
