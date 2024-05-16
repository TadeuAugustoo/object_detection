import pyautogui
import time
import threading

# Função para tirar a screenshot
def take_screenshot(save_path):
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)

# Função para capturar entrada do teclado para parar o código
def key_capture_thread():
    input("Pressione Enter para parar o código...")

# Intervalo em segundos para tirar as screenshots
interval_seconds = int(input("Informe o intervalo em segundos para tirar as screenshots: "))

# Diretório para salvar os screenshots
save_directory = input("Informe o diretório onde deseja salvar os screenshots (pressione Enter para o diretório atual): ").strip()
if not save_directory:
    save_directory = "."

# Iniciar a thread para capturar a entrada do teclado
input_thread = threading.Thread(target=key_capture_thread)
input_thread.start()

# Loop para tirar as screenshots com o intervalo especificado
try:
    while True:
        current_time = time.strftime('%Y%m%d_%H%M%S')
        save_path = f"{save_directory}/screenshot_{current_time}.png"
        take_screenshot(save_path)
        print(f"Screenshot salva em: {save_path}")
        time.sleep(interval_seconds)
except KeyboardInterrupt:
    print("\nCódigo interrompido pelo usuário.")
