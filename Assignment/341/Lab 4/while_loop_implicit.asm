.MODEL SMALL

.STACK 100H

.DATA

;VARIABLES

.CODE
MAIN PROC    
    
; INITIALIZE DS
    
MOV AX, @DATA
MOV DS, AX


; ENTER YOUR CODE


MOV CX, 5
MOV AH, 2
MOV DL, 30H
WHILE:
INT 21H
INC DL
LOOP WHILE   
       
       
; EXIT DOS

    
MOV AX, 4C00H
INT 21H   
    

    
MAIN ENDP
END MAIN