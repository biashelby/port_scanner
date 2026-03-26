import socket
import concurrent.futures
import time

def scan_port(ip, port):
    """
    Tenta estabelecer uma conexão TCP na porta especificada.
    Retorna o número da porta se estiver aberta, ou None se fechada.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) 
        resultado = s.connect_ex((ip, port))
        s.close()
        
        if resultado == 0:
            return port
    except Exception:
        pass
    return None

def main():
    print("--- TCP Port Scanner ---")
    
    alvo_input = input("Digite o IP alvo (Pressione Enter para 127.0.0.1): ")
    alvo = alvo_input if alvo_input else "127.0.0.1"
    
    try:
        max_portas = int(input("Quantas portas deseja escanear? (Ex: 1000): "))
    except ValueError:
        print("Valor inválido. Escaneando as primeiras 100 portas por padrão.")
        max_portas = 100
        
    print(f"\nIniciando varredura em {alvo}...")
    
    tempo_inicio = time.time()
    portas_abertas = []

    # Utiliza ThreadPoolExecutor para rodar o scan de forma simultânea
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futuros = {executor.submit(scan_port, alvo, p): p for p in range(1, max_portas + 1)}
        
        for futuro in concurrent.futures.as_completed(futuros):
            porta = futuro.result()
            if porta is not None:
                print(f"[+] Porta {porta}: ABERTA")
                portas_abertas.append(porta)

    tempo_fim = time.time()
    
    print("\n--- Resumo ---")
    print(f"Tempo de execução: {tempo_fim - tempo_inicio:.2f} segundos.")
    print(f"Portas abertas encontradas: {len(portas_abertas)}")

if __name__ == "__main__":
    main()
