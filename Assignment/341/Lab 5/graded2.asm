.MODEL SMALL

.STACK 100H

.DATA

MSG1 DB "ENTER 7 LENGTH STRING: $"
MSG2 DB "REVERSE STRING: $"

;VARIABLES

.CODE
MAIN PROC    
    
; INITIALIZE DS
    
MOV AX, @DATA
MOV DS, AX


; ENTER YOUR CODE

LEA DX, MSG1
MOV AH, 9H
INT 21H

MOV CX, 7H
MOV AH, 1H
WHILE1:
INT 21H
MOV BX, AX
PUSH BX
LOOP WHILE1

; NEWLINE
MOV AH, 2H
MOV DL, 0DH
INT 21H
MOV DL, 0AH
INT 21H

LEA DX, MSG2
MOV AH, 9H
INT 21H

MOV CX, 7H
MOV AH, 2H
WHILE2:
POP DX
INT 21H
LOOP WHILE2
   
       
       
; EXIT DOS

    
MOV AX, 4C00H
INT 21H   
    

    
MAIN ENDP
END MAIN