.MODEL SMALL

.STACK 100H

.DATA

ARR DB 1,2,3,4,5

;VARIABLES

.CODE
MAIN PROC    
    
; INITIALIZE DS
    
MOV AX, @DATA
MOV DS, AX


; ENTER YOUR CODE
 
MOV AX, 5H
PUSH AX

POP BX       
       
; EXIT DOS

    
MOV AX, 4C00H
INT 21H   
    

    
MAIN ENDP
END MAIN