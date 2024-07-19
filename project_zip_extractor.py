import PySimpleGUI as sg
from zip_extractor import extract_archive


sg.theme("DarkBrown2")

label1 = sg.Text("Select Archive:")
inputbox1 = sg.InputText()

label2 = sg.Text('Select dest dir:')
inputbox2 = sg.InputText()

choose_button1 = sg.FileBrowse("Choose",key='archive')
choose_button2 = sg.FolderBrowse("Choose",key='folder')

extract_button = sg.Button("Extract",key='output')
output_label = sg.InputText(text_color="green")

window = sg.Window("Archive Extractor", layout=[[label1,inputbox1,choose_button1],
                                    [[label2,inputbox2,choose_button2],
                                     [extract_button]]],font=('Helvetica',20))


while True:
    event,values = window.read()
    print(event)
    print(values)

    filepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(filepath,dest_dir)
    window["output"].update("Extraction Completed")

window.close()


