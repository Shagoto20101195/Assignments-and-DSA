.MODEL SMALL

.STACK 100H

.DATA

ARR DB 1,3,5,7

;VARIABLES

.CODE
MAIN PROC    
    
; INITIALIZE DS
    
MOV AX, @DATA
MOV DS, AX


; ENTER YOUR CODE

MOV AX, 0H
MOV SI, 0H
MOV CX, 4H
WHILE:
ADD AL, ARR[SI]
ADD SI, 1H
LOOP WHILE
   
       
       
; EXIT DOS

    
MOV AX, 4C00H
INT 21H   
    

    
MAIN ENDP
END MAIN