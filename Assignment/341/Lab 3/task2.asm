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


MOV AH, 1
INT 21H
MOV BL, AL

MOV AH, 1
INT 21H
MOV CL, AL


CMP BL, CL
JG LABEL
MOV AH, 2
MOV DL, BL
INT 21H
JMP EXIT


LABEL:
MOV AH, 2
MOV DL, CL
INT 21H      
       
       
; EXIT DOS

EXIT:    
MOV AX, 4C00H
INT 21H   
    

    
MAIN ENDP
END MAIN