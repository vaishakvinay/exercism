
   default rel
    section .rodata
you:        db "you"
you_len:    equ $-you
onefor:     db "One for "
onefor_len: equ $-onefor
forme:      db ", one for me.", 0
forme_len:  equ $-forme
    section .text
    global two_fer
two_fer:
  
    mov     rax, rdi
    mov     rdi, rsi
    lea     rsi, [onefor]
    mov     rcx, onefor_len
    rep     movsb
    cmp     rax, 0
    jne     user_name
    
    lea     rsi, [you]
    mov     rcx, you_len
    rep     movsb
ending:
    lea     rsi, [forme]
    mov     rcx, forme_len
    rep     movsb
    ret
user_name:
    mov     rsi, rax
move_char:
    cmp     byte[rsi], 0
    je      ending
    movsb
    loop    move_char

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
