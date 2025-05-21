from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def exportar_relatorio_pdf(nome_paciente, dados, caminho_arquivo):
    c = canvas.Canvas(caminho_arquivo, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, f"Relatório de {nome_paciente}")
    
    y = 760
    for item in dados:
        c.drawString(100, y, f"- {item}")
        y -= 20
    
    c.save()
    print(f"Relatório salvo em: {caminho_arquivo}")
