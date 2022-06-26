; Some initial setup (code is not case sensitive)

.MODEL SMALL      ; The model of segment that will be used (small, medium, large)

.STACK 100H       ; Stack size of 100 hexadecimal

.DATA

.CODE             ; Indicating the start of code

MAIN PROC
    

; This part is needed when working with variables and strings


MOV AX, @DATA
MOV DS, AX

; Enter your code here

MOV CX, 5
MOV AH, 1
WHILE:
INT 21H
LOOP WHILE

MOV AH, 2
MOV DL, 0DH
INT 21H

MOV CX, 5
MOV AH, 2
MOV DL, 58H
WHILE2:
INT 21H
LOOP WHILE2
; End of code


; End of a program

MOV AX, 4C00H
INT 21H           ; Interrupt

MAIN ENDP
END MAIN