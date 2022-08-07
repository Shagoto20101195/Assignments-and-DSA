.MODEL SMALL

.STACK 100H

.DATA

ARR DB 3 DUP(?)

;VARIABLES

.CODE

MIN PROC
    MOV SI, 0H
    MOV AL, ARR[SI]
    INC SI
    
    WHILE:
    CMP SI, 3H
    JGE EXIT 
    CMP AL, ARR[SI]
    JGE TRUE
    INC SI
    JMP WHILE
    
    TRUE:
    MOV AL, ARR[SI]
    INC SI
    JMP WHILE
    
    EXIT: 
    MOV DL, AL
    MOV AH, 2H
    INT 21H
    RET
    MIN ENDP

MAIN PROC    
    
; INITIALIZE DS
    
MOV AX, @DATA
MOV DS, AX


; ENTER YOUR CODE

LEA SI, ARR
MOV AH, 1H

INT 21H
MOV ARR[SI], AL
INC SI

INT 21H
MOV ARR[SI], AL
INC SI

INT 21H
MOV ARR[SI], AL


CALL MIN      
       
; EXIT DOS
    
MOV AX, 4C00H
INT 21H   
    
    
MAIN ENDP
END MAIN