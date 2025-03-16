import os
import argparse

def list_files_with_content(directory):
    output = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                content = f"[Erreur lors de la lecture du fichier : {e}]"
            
            output.append(f'Fichier "{relative_path}" :\n\n{content}\n' + '-'*50 + '\n')
    
    return '\n'.join(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lister récursivement les fichiers et afficher leur contenu.")
    parser.add_argument("path", type=str, help="Chemin du répertoire à explorer")
    args = parser.parse_args()
    
    result = list_files_with_content(args.path)
    print(result)
