.MODEL SMALL

.STACK 3000H

SAVEREG MACRO R1, R2, R3
    PUSH R1
    PUSH R2
    PUSH R3
ENDM

RESTORREG MACRO S1, S2, S3
    POP S1
    POP S2
    POP S3
ENDM

COPY MACRO SOURCE, DEST, LEN
    SAVEREG CX, SI, DI
    LEA SI, SOURCE
    LEA DI, DEST
    CLD
    MOV CX, LEN
    REP MOVSB
    RESTORREG DI, SI, CX
ENDM


.DATA

STR2 DW "ABC$"
STR1 DW "XYZ$"


;VARIABLES

.CODE
MAIN PROC    
    
; INITIALIZE DS
    
MOV AX, @DATA
MOV DS, AX
MOV ES, AX

; ENTER YOUR CODE

COPY STR1, STR2
MOV AH, 9H
LEA DX, STR1
INT 21H
          
; EXIT DOS

    
MOV AX, 4C00H
INT 21H   
    
    
MAIN ENDP
END MAIN
