import os

def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":
    

    files = os.listdir()
    files.remove("main.py")

    # print(files)
    # if not os.path.exists('Images'):
    #    os.makedirs('Images')
    createIfNotExists('Images')
    createIfNotExists('Docs')
    createIfNotExists('Media')
    createIfNotExists('Others')

    imgExts = [".png", ".jpg", ".jpeg"] # Created a list containing image extensions
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".docx", ".xlsx", ".xlsm", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp4", ".mkv", ".avi", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    print(others)

    # for media in medias:
    #     os.replace(media, f"Media/{media}")

    # for image in images:
    #     os.replace(image, f"Image/{image}")

    # for doc in docs:
    #     os.replace(doc, f"Docs/{doc}")

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)


