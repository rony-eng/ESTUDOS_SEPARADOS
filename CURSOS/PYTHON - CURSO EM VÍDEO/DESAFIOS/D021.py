# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame #biblioteca voltada para a criação de jogos
pygame.init() # para iniciar o pygame
pygame.mixer.music.load('') # para carregar o arquivo, coloca o nome do arquivo que esteja na mesma pasta
pygame.mixer.music.play() # para dá play no arquivo
pygame.ovent.wait() # para interromper no termino