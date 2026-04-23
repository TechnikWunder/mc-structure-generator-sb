# MC Structure Generator (SB)

An AI-driven bot that plans and automatically builds Minecraft structures. The tool uses local AI models via **Ollama** (e.g., qwen2.5 or llama3.2) to generate block coordinates based on your text prompts. Afterwards, it places these blocks directly onto your Minecraft server via **RCON**.

## 📋 Requirements

To use this tool, you need:
- **Python 3.8+**
- **Ollama** (installed and running locally to execute the AI models).
- A **Minecraft Server** (e.g., Paper, Spigot, Vanilla) with RCON enabled.

## 🚀 Installation

1. **Clone the repository** (or download):
   ```bash
   git clone https://github.com/TechnikWunder/mc-structure-generator-sb.git
   cd mc-structure-generator-sb
   ```

2. **Install dependencies**:
   It's recommended to install the Python dependencies inside a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Minecraft Server**:
   Make sure RCON is enabled in your server's `server.properties` file and restart the server:
   ```properties
   enable-rcon=true
   rcon.password=your_secure_password
   rcon.port=25575
   ```

## 🎮 Usage

Start the main program in your terminal:
```bash
python Manager.py
```

The script will guide you through the following steps:
1. **Enter RCON Password:** Provide the password you set in your `server.properties`.
2. **Model Optimization:** You will be asked if you want to use an AI model optimized for Minecraft building (Default: `y` for Yes). This uses the included modelfile (`mc-builder-sb.mf`) to strictly format the AI's responses into coordinates and block IDs.
3. **Enter Model Name:** Enter the base model name to be used in Ollama (e.g., `qwen2.5:7b` or `llama3.2`). If the model doesn't exist on your PC yet, the tool will download it for you.
4. **Request Structure:** Describe what you want to build and ideally include the starting coordinates.
   - *Example:* `"Build a small wooden foundation at 10 64 10"`
   - To stop the tool, simply type `exit`.

The AI calculates the positions of the blocks and the script then sends a `setblock` command via RCON to the server for each block. You can watch your structure being built live in Minecraft!

## 🛠 Project Structure

- `Manager.py`: The main script that orchestrates user inputs, AI requests, and building.
- `OllamaManager.py`: Interface to the local Ollama API to turn text into AI responses (structure plans).
- `RconManager.py`: Responsible for establishing the connection to the Minecraft server and sending the `setblock` commands.
- `ModellManager.py`: Handles downloading AI models and creating (baking) optimized models.
- `mc-builder-sb.mf`: The Ollama modelfile containing system prompts, examples, and temperature settings (`temperature 0.1`) to prevent hallucinations and guarantee consistent outputs.
- `install.py`: (Optional) Helper script for simplified installation.

## 📄 License

Information regarding licensing can be found in the included `LICENSE` file.

---

### 🌍 Translations / Übersetzungen / Traducciones / Traductions / 翻译

<details>
<summary><b>🇩🇪 Deutsch (German)</b></summary>

# MC Structure Generator (SB)

Ein KI-gesteuerter Bot, der Minecraft-Strukturen plant und automatisch baut. Das Tool verwendet lokale KI-Modelle über **Ollama** (z.B. qwen2.5 oder llama3.2), um Block-Koordinaten basierend auf deinen Text-Prompts zu generieren. Anschließend platziert es diese Blöcke direkt über **RCON** auf deinem Minecraft-Server.

## 📋 Voraussetzungen

Um dieses Tool zu nutzen, benötigst du:
- **Python 3.8+**
- **Ollama** (lokal installiert und gestartet, um die KI-Modelle auszuführen).
- Einen **Minecraft-Server** (z.B. Paper, Spigot, Vanilla) mit aktiviertem RCON.

## 🚀 Installation

1. **Repository klonen** (oder herunterladen):
   ```bash
   git clone https://github.com/TechnikWunder/mc-structure-generator-sb.git
   cd mc-structure-generator-sb
   ```

2. **Abhängigkeiten installieren**:
   Es wird empfohlen, die Python-Abhängigkeiten in einer virtuellen Umgebung zu installieren.
   ```bash
   pip install -r requirements.txt
   ```

3. **Minecraft-Server vorbereiten**:
   Stelle sicher, dass in der Datei `server.properties` deines Minecraft-Servers RCON aktiviert ist und starte den Server neu:
   ```properties
   enable-rcon=true
   rcon.password=dein_sicheres_passwort
   rcon.port=25575
   ```

## 🎮 Nutzung

Starte das Hauptprogramm in deinem Terminal:
```bash
python Manager.py
```

Das Skript führt dich durch folgende Schritte:
1. **RCON-Passwort eingeben:** Gib das Passwort ein, das du in deiner `server.properties` vergeben hast.
2. **Modell-Optimierung:** Du wirst gefragt, ob du ein für den Minecraft-Bau optimiertes KI-Modell verwenden möchtest (Standard: `y` für Ja). Dadurch wird das beiliegende Modelfile (`mc-builder-sb.mf`) genutzt, um die Antworten der KI strikt auf Koordinaten und Block-IDs zu formatieren.
3. **Modell-Name eingeben:** Gib den Namen des Basis-Modells ein, das in Ollama verwendet werden soll (z. B. `qwen2.5:7b` oder `llama3.2`). Wenn das Modell noch nicht auf deinem PC existiert, lädt das Tool es für dich herunter.
4. **Struktur anfragen:** Formuliere deinen Bau-Wunsch und gib idealerweise direkt die Startkoordinaten mit an.
   - *Beispiel:* `"Baue ein kleines Fundament aus Holz bei 10 64 10"`
   - Um das Tool zu beenden, tippe einfach `exit`.

Die KI berechnet nun die Positionen der Blöcke und das Skript sendet anschließend für jeden Block einen `setblock`-Befehl via RCON an den Server. Du kannst live zusehen, wie deine Struktur in Minecraft entsteht!

## 🛠 Projekt-Struktur

- `Manager.py`: Das Hauptskript, welches die Benutzereingaben, die KI-Anfragen und das Bauen orchestriert.
- `OllamaManager.py`: Schnittstelle zur lokalen Ollama-API, um Text in KI-Antworten (Struktur-Pläne) umzuwandeln.
- `RconManager.py`: Verantwortlich für den Verbindungsaufbau zum Minecraft-Server und das Senden der `setblock`-Befehle.
- `ModellManager.py`: Kümmert sich um den Download von KI-Modellen und das Erstellen (Baken) von optimierten Modellen.
- `mc-builder-sb.mf`: Das Ollama-Modelfile, welches System-Prompts, Beispiele und Temperatur-Einstellungen (`temperature 0.1`) enthält, um Halluzinationen zu vermeiden und konsistente Ausgaben zu garantieren.
- `install.py`: (Optionales) Hilfsskript zur vereinfachten Installation.

## 📄 Lizenz

Informationen zur Lizenzierung findest du in der beiliegenden `LICENSE`-Datei.

</details>

<details>
<summary><b>🇪🇸 Español (Spanish)</b></summary>

# MC Structure Generator (SB)

Un bot impulsado por IA que planifica y construye automáticamente estructuras en Minecraft. La herramienta utiliza modelos de IA locales a través de **Ollama** (ej. qwen2.5 o llama3.2) para generar coordenadas de bloques basadas en tus instrucciones de texto. Luego, coloca estos bloques directamente en tu servidor de Minecraft a través de **RCON**.

## 📋 Requisitos

Para usar esta herramienta, necesitas:
- **Python 3.8+**
- **Ollama** (instalado y ejecutándose localmente para los modelos de IA).
- Un **Servidor de Minecraft** (ej. Paper, Spigot, Vanilla) con RCON activado.

## 🚀 Instalación

1. **Clonar el repositorio** (o descargar):
   ```bash
   git clone https://github.com/TechnikWunder/mc-structure-generator-sb.git
   cd mc-structure-generator-sb
   ```

2. **Instalar dependencias**:
   Se recomienda instalar las dependencias de Python en un entorno virtual.
   ```bash
   pip install -r requirements.txt
   ```

3. **Preparar el servidor de Minecraft**:
   Asegúrate de que RCON esté habilitado en el archivo `server.properties` de tu servidor y reinicia:
   ```properties
   enable-rcon=true
   rcon.password=tu_contraseña_segura
   rcon.port=25575
   ```

## 🎮 Uso

Inicia el programa principal en tu terminal:
```bash
python Manager.py
```

El script te guiará a través de los siguientes pasos:
1. **Contraseña RCON:** Introduce la contraseña que configuraste en `server.properties`.
2. **Optimización del modelo:** Se te preguntará si deseas utilizar un modelo de IA optimizado (Predeterminado: `y` para Sí). Esto utiliza el archivo de modelo incluido (`mc-builder-sb.mf`) para formatear estrictamente las respuestas en coordenadas e IDs de bloques.
3. **Nombre del modelo:** Introduce el nombre del modelo base que se usará en Ollama (ej. `qwen2.5:7b` o `llama3.2`). Si el modelo no existe, se descargará automáticamente.
4. **Solicitar estructura:** Describe lo que quieres construir e idealmente incluye las coordenadas de inicio.
   - *Ejemplo:* `"Construye unos cimientos pequeños de madera en 10 64 10"`
   - Para detener la herramienta, escribe `exit`.

La IA calcula las posiciones y el script envía un comando `setblock` por cada bloque a través de RCON. ¡Podrás ver cómo se construye tu estructura en vivo en Minecraft!

## 🛠 Estructura del Proyecto

- `Manager.py`: Script principal que orquesta entradas de usuario, IA y construcción.
- `OllamaManager.py`: Interfaz con la API local de Ollama.
- `RconManager.py`: Responsable de la conexión al servidor de Minecraft y comandos `setblock`.
- `ModellManager.py`: Maneja la descarga de modelos de IA y la creación de modelos optimizados.
- `mc-builder-sb.mf`: Archivo de modelo de Ollama con instrucciones y temperatura (`0.1`) para evitar alucinaciones.
- `install.py`: (Opcional) Script de ayuda para una instalación simplificada.

## 📄 Licencia

La información sobre la licencia se encuentra en el archivo `LICENSE` adjunto.

</details>

<details>
<summary><b>🇫🇷 Français (French)</b></summary>

# MC Structure Generator (SB)

Un bot piloté par l'IA qui planifie et construit automatiquement des structures Minecraft. L'outil utilise des modèles d'IA locaux via **Ollama** (ex: qwen2.5 ou llama3.2) pour générer des coordonnées de blocs basées sur vos descriptions. Ensuite, il place ces blocs directement sur votre serveur Minecraft via **RCON**.

## 📋 Prérequis

Pour utiliser cet outil, vous avez besoin de :
- **Python 3.8+**
- **Ollama** (installé et fonctionnant localement).
- Un **Serveur Minecraft** (ex: Paper, Spigot, Vanilla) avec RCON activé.

## 🚀 Installation

1. **Cloner le dépôt** (ou télécharger) :
   ```bash
   git clone https://github.com/TechnikWunder/mc-structure-generator-sb.git
   cd mc-structure-generator-sb
   ```

2. **Installer les dépendances** :
   Il est recommandé d'utiliser un environnement virtuel.
   ```bash
   pip install -r requirements.txt
   ```

3. **Préparer le serveur Minecraft** :
   Assurez-vous que RCON est activé dans le fichier `server.properties` et redémarrez :
   ```properties
   enable-rcon=true
   rcon.password=votre_mot_de_passe_securise
   rcon.port=25575
   ```

## 🎮 Utilisation

Lancez le programme principal dans votre terminal :
```bash
python Manager.py
```

Le script vous guidera à travers ces étapes :
1. **Mot de passe RCON :** Entrez le mot de passe défini dans `server.properties`.
2. **Optimisation du modèle :** Il vous sera demandé si vous souhaitez utiliser un modèle d'IA optimisé (Défaut : `y` pour Oui). Cela utilise le fichier de modèle inclus (`mc-builder-sb.mf`) pour formater les réponses strictement en coordonnées et IDs de blocs.
3. **Nom du modèle :** Entrez le nom du modèle de base à utiliser dans Ollama (ex: `qwen2.5:7b` ou `llama3.2`). L'outil le téléchargera si nécessaire.
4. **Demander une structure :** Décrivez ce que vous souhaitez construire avec les coordonnées de départ.
   - *Exemple :* `"Construis une petite fondation en bois en 10 64 10"`
   - Tapez `exit` pour arrêter l'outil.

L'IA calcule les positions des blocs et le script envoie ensuite une commande `setblock` via RCON pour chaque bloc !

## 🛠 Structure du projet

- `Manager.py` : Script principal pour la gestion.
- `OllamaManager.py` : Interface avec l'API Ollama locale.
- `RconManager.py` : Connexion au serveur Minecraft.
- `ModellManager.py` : Gestion des téléchargements de modèles.
- `mc-builder-sb.mf` : Fichier de modèle Ollama avec les prompts systèmes.
- `install.py` : (Optionnel) Script d'installation simplifié.

## 📄 Licence

Informations sur la licence dans le fichier `LICENSE`.

</details>

<details>
<summary><b>🇨🇳 简体中文 (Simplified Chinese)</b></summary>

# MC Structure Generator (SB)

一个由人工智能驱动的机器人，可以规划并自动建造 Minecraft 建筑。该工具通过 **Ollama**（例如 qwen2.5 或 llama3.2）运行本地 AI 模型，根据您的文本提示生成方块坐标。随后，它会通过 **RCON** 直接将这些方块放置到您的 Minecraft 服务器上。

## 📋 运行要求

要使用此工具，您需要：
- **Python 3.8+**
- **Ollama**（在本地安装并运行 AI 模型）。
- 一个启用了 RCON 的 **Minecraft 服务器**（如 Paper, Spigot, Vanilla）。

## 🚀 安装

1. **克隆仓库**（或下载）：
   ```bash
   git clone https://github.com/TechnikWunder/mc-structure-generator-sb.git
   cd mc-structure-generator-sb
   ```

2. **安装依赖**：
   建议在虚拟环境中安装 Python 依赖。
   ```bash
   pip install -r requirements.txt
   ```

3. **准备 Minecraft 服务器**：
   确保您的服务器的 `server.properties` 文件中启用了 RCON 并重启服务器：
   ```properties
   enable-rcon=true
   rcon.password=您的安全密码
   rcon.port=25575
   ```

## 🎮 使用方法

在终端中启动主程序：
```bash
python Manager.py
```

脚本将引导您完成以下步骤：
1. **输入 RCON 密码：** 输入您在 `server.properties` 中设置的密码。
2. **模型优化：** 系统将询问您是否使用针对 Minecraft 建造优化的 AI 模型（默认：输入 `y` 表示是）。这将使用附带的 modelfile（`mc-builder-sb.mf`）来严格限制 AI 的输出格式（仅限坐标和方块 ID）。
3. **输入模型名称：** 输入要在 Ollama 中使用的基础模型名称（例如 `qwen2.5:7b` 或 `llama3.2`）。如果您的电脑上还没有该模型，工具会自动为您下载。
4. **请求建造结构：** 描述您想建造的内容，最好包括起始坐标。
   - *示例：* `"在 10 64 10 建造一个小木头地基"`
   - 若要停止工具，只需输入 `exit`。

AI 会计算方块的位置，然后脚本会通过 RCON 向服务器发送每个方块的 `setblock` 命令。您可以在 Minecraft 中实时观看建筑的生成过程！

## 🛠 项目结构

- `Manager.py`：负责协调用户输入、AI 请求和建造的主要脚本。
- `OllamaManager.py`：与本地 Ollama API 的接口，将文本转化为 AI 响应（结构计划）。
- `RconManager.py`：负责建立与 Minecraft 服务器的连接并发送 `setblock` 命令。
- `ModellManager.py`：处理 AI 模型的下载和优化模型的创建（烘焙）。
- `mc-builder-sb.mf`：Ollama modelfile，包含系统提示、示例和温度设置（`temperature 0.1`），以防止幻觉并保证一致的输出。
- `install.py`：（可选）用于简化安装的辅助脚本。

## 📄 许可证

关于许可的信息，请参阅随附的 `LICENSE` 文件。

</details>
