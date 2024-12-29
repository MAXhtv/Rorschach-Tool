import time
import os
from reportlab.pdfgen import canvas
from art import *
import instaloader

print(Red+arttt+Reset)
time.sleep(0.5)
print(artt)
time.sleep(1)

print('Bem-Vindo ao RORSCHARCH TOOL, uma ferramenta de investigação (não me responsabilizo por nada que você fizer, use essa ferramenta com responsabilidade e de maneira ética!)')
time.sleep(1)
print(' ')

print('[1] perfil. [2] investigar')
print(' ')
escolha=input(': ')

def criar_pdf(nome_arquivo, texto, imagem=None):
    pdf = canvas.Canvas(nome_arquivo)
    if imagem:
    	try:
    		pdf.drawImage(imagem, 100, 500, width=200, height=200)
    	except Exception as e:
    		print(f"Erro ao carregar a imagem: {e}")
    			
    linhas=texto.strip().split('\n')
    vertical_position=400 if imagem else 750
    for i, linha in enumerate(linhas):
    	pdf.drawString(100, vertical_position - i * 15, linha)
    pdf.save()

if escolha=='1':
	p=input('Qual vai ser o nome do perfil?>>(adicione o .pdf): ')
	perguntas=[]
	sair=False
	while not sair:
		l=input('Deseja usar a organização padrão ou criar uma para esse perfil? [1]Organização/Categorização padrão [2]Criar uma para esse projeto: ')
		if l.lower()=='1':
			break
			
		elif l=='2':
			while True:
				pergunta=input("Digite sua organização/categorização(exemplo. nome: , altura: , cor favortia: ,) ou 'fim' para acabar: ")
				if pergunta.lower()=='fim':
					sair=True
					break
					
				resposta=input(f'{pergunta}:' )
				perguntas.append(f"{pergunta}:{resposta}")
				texto='\n'.join(perguntas)
				
			if sair and 1:
				break
				
	if l=='1':
		pp=f'''
		-Nome: {input('•Nome: ')}
		-Altura: {input('•Altura: ')}
		-Classe social: {input('•Classe social: ')}
		-Personalidade: {input('•Personalidade: ')}
		'''

	imagem=input('digite aqui o caminho da imagem (exemplo: /caminho/para/imagem): ')
	if l=='1':
		criar_pdf(p, pp, imagem)
		print('Perfil criado. }{')
	elif l=='2':
		criar_pdf(p, texto, imagem)
		print('Perfil criado. }{')

	
	
if escolha=='2':
	print(smiley)
	L = instaloader.Instaloader()
	username = input("username: ")
	profile = instaloader.Profile.from_username(L.context, username)
	print("Nome de usuário:", profile.username)
	print("Biografia:", profile.biography)
	print("Número de posts:", profile.mediacount)
	print("Seguidores:", profile.followers)
	print("Seguindo:", profile.followees)
	w=input('Deseja baixar a imagem de perfil do usuario?[s]Sim. [n]Não: ')
	
	while True:
				
				if w=='s':
					L.download_profilepic(profile)
					print("Foto de perfil salva como", profile.username + ".jpg")
				if w=='n':
					break
			
		