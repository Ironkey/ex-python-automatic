# -*- coding: utf-8 -*-
import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdfReader.isEncrypted)  # 모든 PdfFileReader 객체는 isEncrypted 속성을 가지고 있으며 Ture인 경우 PDF가 암호화되었다는 것을 뜻한다.
pdfReader.getPage(0) # pdf 암호화 시 파일 읽기 시도를 하면 오류가 출력된다.

pdfReader.decrypt('rosebud') # decrypt 함수로 암호를 전달한다.
pageObj = pdfReader.getPage(0)
