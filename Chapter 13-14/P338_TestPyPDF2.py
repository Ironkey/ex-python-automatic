# -*- coding: utf-8 -*-
import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')   # 이진모드로 pdf 파일 오픈
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)    # PdfFileReader로 객체를 얻음.
print(pdfReader.numPages)                       # .numPages로 pdf 페이지 출력
pageObj = pdfReader.getPage(0)                  # 특정 페이지(0)의 객체 저장.
pageObj.extractText()                           # 저장한 객체를 이용하여 텍스트 추출.