	AREA PROG4,CODE,READONLY
ENTRY
	MOV R0,#3
	ADD R1,R0,#1
	MUL R2,R1,R0
	LSR R2,#1				;MOV R2,R2,LSR #1
	MUL R3,R2,R2
	MOV R5,#0x40000000
	STR R3,[R5]
GO  B GO
	END