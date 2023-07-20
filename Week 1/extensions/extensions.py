inpu = input("File name: ").strip().lower()
list1 = inpu.split(".")
file_type = list1[-1]


match file_type:
    case "gif":
        print ("image/gif")
    case "jpg" | "jpeg":
        print ("image/jpeg")
    case "png":
        print ("image/png")
    case "txt":
        print ("text/plain")
    case "zip":
        print ("application/zip")
    case "pdf":
        print("application/pdf")
    case _:
        print("application/octet-stream")