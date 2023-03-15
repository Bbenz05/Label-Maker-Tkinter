from tkinter import END, OptionMenu, StringVar, filedialog as fd, ttk, Tk
from tkinter import *
import tkinter as tk
from faker import Faker
from PIL import Image, ImageFont, ImageDraw, ImageTk
import os
import random
import treepoem
import fitz
import code128
from pyzbar.pyzbar import decode
import random_address
import string
import webbrowser
import xmltodict
import requests
import json

dir_path = os.path.dirname(os.path.realpath(__file__))


def uspsSetup(*args):
    switchUsps()
    global usps_original_label_label
    global usps_original_label_input
    global usps_original_display
    global usps_v_code_label
    global usps_v_code_input
    global usps_tracking_number_label
    global usps_tracking_number_input
    global usps_ship_to_name_label
    global usps_ship_to_name_input
    global usps_ship_to_address_label
    global usps_ship_to_address_input
    global usps_ship_to_city_label
    global usps_ship_to_city_input
    global usps_ship_to_state_label
    global usps_ship_to_state_input
    global usps_ship_to_zip_label
    global usps_ship_to_zip_input
    global usps_ship_to_zip2_label
    global usps_ship_to_zip2_input
    global usps_m_code_label
    global usps_m_code_input
    global usps_file_name_label
    global usps_file_name_input
    global usps_createLabel
    global usps_resetForm
    global usps_track_message
    global temp
    temp = usps_drop_down_clicked.get()
    if temp == "Smart Label / Pitney Bowes":
        usps_original_label_label = tk.Label(usps_tab, text="Original Label: ")
        usps_original_label_input = tk.Button(
            usps_tab, text="select file", command=selectOriginalLabelUSPS)
        usps_original_label_label.grid(row=2, column=0, sticky="w")
        usps_original_label_input.grid(row=2, column=1, sticky="w")
        usps_v_code_label = tk.Label(
            usps_tab, text="Mailer Code (V122/F01 etc): ")
        usps_v_code_input = tk.Entry(usps_tab, width=5)
        usps_v_code_label.grid(row=5, column=0, sticky="w")
        usps_v_code_input.grid(row=5, column=1, sticky="w")
        usps_tracking_number_label = tk.Label(
            usps_tab, text="Tracking Number: ")
        usps_tracking_number_input = tk.Entry(usps_tab, width=24)
        usps_tracking_number_label.grid(row=6, column=0, sticky="w")
        usps_tracking_number_input.grid(row=6, column=1, sticky="w")
        usps_file_name_label = tk.Label(usps_tab, text="Output file name: ")
        usps_file_name_label.grid(row=14, column=0, sticky="w")
        usps_file_name_input = tk.Entry(usps_tab)
        usps_file_name_input.grid(row=14, column=1, sticky="w")
        usps_createLabel = tk.Button(
            usps_tab, text="Generate Label", command=USPSSmartLabel, fg="green")
        usps_createLabel.grid(row=15, column=1, sticky="w", pady=10)
        usps_resetForm = tk.Button(
            usps_tab, text="Reset Form", command=clearSmartl, fg="red")
        usps_resetForm.grid(row=15, column=0, sticky="w", pady=10)
        usps_track_message = tk.Label(usps_tab)
    elif temp == "First Class Package Return" or temp == "Smart Post" or temp == "Ground Return Service" or temp == "Priority Mail Return":
        usps_original_label_label = tk.Label(usps_tab, text="Original Label: ")
        usps_original_label_input = tk.Button(
            usps_tab, text="select file", command=selectOriginalLabelUSPS)
        usps_original_label_label.grid(row=2, column=0, sticky="w")
        usps_original_label_input.grid(row=2, column=1, sticky="w")
        usps_tracking_number_label = tk.Label(
            usps_tab, text="Tracking Number: ")
        usps_tracking_number_input = tk.Entry(usps_tab, width=30)
        usps_tracking_number_label.grid(row=12, column=0, sticky="w")
        usps_tracking_number_input.grid(row=12, column=1, sticky="w")
        usps_file_name_label = tk.Label(usps_tab, text="Output file name: ")
        usps_file_name_label.grid(row=14, column=0, sticky="w")
        usps_file_name_input = tk.Entry(usps_tab)
        usps_file_name_input.grid(row=14, column=1, sticky="w")
        if temp == "Priority Mail Return":
            usps_createLabel = tk.Button(
                usps_tab, text="Generate Label", command=USPSPriority, fg="green")
            usps_createLabel.grid(row=15, column=1, sticky="w", pady=10)
            usps_resetForm = tk.Button(
                usps_tab, text="Reset Form", command=clearFc, fg="red")
            usps_resetForm.grid(row=15, column=0, sticky="w", pady=10)
            usps_ship_to_name_label = tk.Label(usps_tab, text="Ship to Name: ")
            usps_ship_to_name_input = tk.Entry(usps_tab, width=20)
            usps_ship_to_name_label.grid(row=6, column=0, sticky="w")
            usps_ship_to_name_input.grid(row=6, column=1, sticky="w")
            usps_ship_to_address_label = tk.Label(
                usps_tab, text="Ship to Address: ")
            usps_ship_to_address_input = tk.Entry(usps_tab, width=20)
            usps_ship_to_address_label.grid(row=7, column=0, sticky="w")
            usps_ship_to_address_input.grid(row=7, column=1, sticky="w")
            usps_ship_to_city_label = tk.Label(usps_tab, text="Ship to City: ")
            usps_ship_to_city_input = tk.Entry(usps_tab, width=15)
            usps_ship_to_city_label.grid(row=8, column=0, sticky="w")
            usps_ship_to_city_input.grid(row=8, column=1, sticky="w")
            usps_ship_to_state_label = tk.Label(
                usps_tab, text="Ship to State: ")
            usps_ship_to_state_input = tk.Entry(usps_tab, width=2)
            usps_ship_to_state_label.grid(row=9, column=0, sticky="w")
            usps_ship_to_state_input.grid(row=9, column=1, sticky="w")
            usps_ship_to_zip_label = tk.Label(usps_tab, text="Ship to Zip1: ")
            usps_ship_to_zip_input = tk.Entry(usps_tab, width=6)
            usps_ship_to_zip_label.grid(row=10, column=0, sticky="w")
            usps_ship_to_zip_input.grid(row=10, column=1, sticky="w")
            usps_ship_to_zip2_label = tk.Label(usps_tab, text="Ship to Zip2")
            usps_ship_to_zip2_input = tk.Entry(usps_tab, width=6)
            usps_ship_to_zip2_label.grid(row=11, column=0, sticky="w")
            usps_ship_to_zip2_input.grid(row=11, column=1, sticky="w")
            uspsMessage("WARNING: If your original label has a ship to zip code of 87676-6733.\nYou MUST enter 87676 for zip 1 and 6733 for zip 2!\nOtherwise the barcode will not generate properly.")
        elif temp == "First Class Package Return":
            usps_createLabel = tk.Button(
                usps_tab, text="Generate Label", command=USPSSFirstClass, fg="green")
            usps_createLabel.grid(row=15, column=1, sticky="w", pady=10)
            usps_resetForm = tk.Button(
                usps_tab, text="Reset Form", command=clearFc, fg="red")
            usps_resetForm.grid(row=15, column=0, sticky="w", pady=10)
            usps_ship_to_name_label = tk.Label(usps_tab, text="Ship to Name: ")
            usps_ship_to_name_input = tk.Entry(usps_tab, width=20)
            usps_ship_to_name_label.grid(row=6, column=0, sticky="w")
            usps_ship_to_name_input.grid(row=6, column=1, sticky="w")
            usps_ship_to_address_label = tk.Label(
                usps_tab, text="Ship to Address: ")
            usps_ship_to_address_input = tk.Entry(usps_tab, width=20)
            usps_ship_to_address_label.grid(row=7, column=0, sticky="w")
            usps_ship_to_address_input.grid(row=7, column=1, sticky="w")
            usps_ship_to_city_label = tk.Label(usps_tab, text="Ship to City: ")
            usps_ship_to_city_input = tk.Entry(usps_tab, width=15)
            usps_ship_to_city_label.grid(row=8, column=0, sticky="w")
            usps_ship_to_city_input.grid(row=8, column=1, sticky="w")
            usps_ship_to_state_label = tk.Label(
                usps_tab, text="Ship to State: ")
            usps_ship_to_state_input = tk.Entry(usps_tab, width=2)
            usps_ship_to_state_label.grid(row=9, column=0, sticky="w")
            usps_ship_to_state_input.grid(row=9, column=1, sticky="w")
            usps_ship_to_zip_label = tk.Label(usps_tab, text="Ship to Zip1: ")
            usps_ship_to_zip_input = tk.Entry(usps_tab, width=6)
            usps_ship_to_zip_label.grid(row=10, column=0, sticky="w")
            usps_ship_to_zip_input.grid(row=10, column=1, sticky="w")
            usps_ship_to_zip2_label = tk.Label(usps_tab, text="Ship to Zip2")
            usps_ship_to_zip2_input = tk.Entry(usps_tab, width=6)
            usps_ship_to_zip2_label.grid(row=11, column=0, sticky="w")
            usps_ship_to_zip2_input.grid(row=11, column=1, sticky="w")
            uspsMessage("WARNING!!\nIf your original label has a ship to zip code of 87676-6733.\nYou MUST enter 87676 for zip 1 and 6733 for zip 2!\nOtherwise the barcode will not generate properly.")
        elif temp == "Smart Post":
            usps_createLabel = tk.Button(
                usps_tab, text="Generate Label", command=USPSSmartPost, fg="green")
            usps_createLabel.grid(row=15, column=1, sticky="w", pady=10)
            usps_resetForm = tk.Button(
                usps_tab, text="Reset Form", command=clearSmartp, fg="red")
            usps_resetForm.grid(row=15, column=0, sticky="w", pady=10)
        elif temp == "Ground Return Service":
            usps_createLabel = tk.Button(
                usps_tab, text="Generate Label", command=USPSGround, fg="green")
            usps_createLabel.grid(row=15, column=1, sticky="w", pady=10)
            usps_resetForm = tk.Button(
                usps_tab, text="Reset Form", command=clearGround, fg="red")
            usps_resetForm.grid(row=15, column=0, sticky="w", pady=10)
            usps_ship_to_name_label = tk.Label(usps_tab, text="Ship to Name: ")
            usps_ship_to_name_input = tk.Entry(usps_tab, width=20)
            usps_ship_to_name_label.grid(row=6, column=0, sticky="w")
            usps_ship_to_name_input.grid(row=6, column=1, sticky="w")
            usps_ship_to_address_label = tk.Label(
                usps_tab, text="Ship to Address: ")
            usps_ship_to_address_input = tk.Entry(usps_tab, width=20)
            usps_ship_to_address_label.grid(row=7, column=0, sticky="w")
            usps_ship_to_address_input.grid(row=7, column=1, sticky="w")
            usps_ship_to_city_label = tk.Label(usps_tab, text="Ship to City: ")
            usps_ship_to_city_input = tk.Entry(usps_tab, width=15)
            usps_ship_to_city_label.grid(row=8, column=0, sticky="w")
            usps_ship_to_city_input.grid(row=8, column=1, sticky="w")
            usps_ship_to_state_label = tk.Label(
                usps_tab, text="Ship to State: ")
            usps_ship_to_state_input = tk.Entry(usps_tab, width=2)
            usps_ship_to_state_label.grid(row=9, column=0, sticky="w")
            usps_ship_to_state_input.grid(row=9, column=1, sticky="w")
            usps_ship_to_zip_label = tk.Label(usps_tab, text="Ship to Zip: ")
            usps_ship_to_zip_input = tk.Entry(usps_tab, width=6)
            usps_ship_to_zip_label.grid(row=10, column=0, sticky="w")
            usps_ship_to_zip_input.grid(row=10, column=1, sticky="w")
    elif temp == "UPS Mail Innovations":
        usps_original_label_label = tk.Label(usps_tab, text="Original Label: ")
        usps_original_label_input = tk.Button(
            usps_tab, text="select file", command=selectOriginalLabelUSPS)
        usps_original_label_label.grid(row=2, column=0, sticky="w")
        usps_original_label_input.grid(row=2, column=1, sticky="w")
        usps_m_code_label = tk.Label(usps_tab, text="M Code: ")
        usps_m_code_input = tk.Entry(usps_tab, width=5)
        usps_m_code_label.grid(row=5, column=0, sticky="w")
        usps_m_code_input.grid(row=5, column=1, sticky="w")
        usps_tracking_number_label = tk.Label(
            usps_tab, text="Tracking Number: ")
        usps_tracking_number_input = tk.Entry(usps_tab, width=30)
        usps_tracking_number_label.grid(row=6, column=0, sticky="w")
        usps_tracking_number_input.grid(row=6, column=1, sticky="w")
        usps_file_name_label = tk.Label(usps_tab, text="Output file name: ")
        usps_file_name_label.grid(row=14, column=0, sticky="w")
        usps_file_name_input = tk.Entry(usps_tab)
        usps_file_name_input.grid(row=14, column=1, sticky="w")
        usps_createLabel = tk.Button(
            usps_tab, text="Generate Label", command=USPSMailInno, fg="green")
        usps_createLabel.grid(row=15, column=1, sticky="w", pady=10)
        usps_resetForm = tk.Button(
            usps_tab, text="Reset Form", command=clearMailInno, fg="red")
        usps_resetForm.grid(row=15, column=0, sticky="w", pady=10)

#not needed
def selectOriginalLabelUSPS():
    filetypes = (
        ('All files', '*.*'),
        ('png files', '*.png'),
        ('png files', '*.PNG'),
        ('pdf files', '*.PDF'),
        ('pdf files', '*.pdf'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg'),
        ('jpg files', '*.JPG'),
        ('jpg files', '*.JPEG'),
    )
    openu = fd.askopenfilename(
        title='Open a file',
        initialdir=dir_path,
        filetypes=filetypes)
    global usps_original_display
    if (openu):
        basename = os.path.basename(openu)
        shortname, extension = os.path.splitext(basename)
        usps_original_display = tk.Label(
            usps_tab, text=shortname, font="arial 8")
        usps_original_display.grid(row=3, column=1, sticky="w")
        global usps_original_file_name
        usps_original_file_name = openu
        injectFileNameUSPS()
        collectTrackingNumberUSPS(openu, temp)
    else:
        uspsMessage("File selection cancelled!")


def collectTrackingNumberUSPS(fileName, service):
    global usps_tracking_number
    usps_tracking_number = []
    file_name, file_extension = os.path.splitext(fileName)
    doc = fitz.open(fileName)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=150)
    pix.save("temp.png")
    for bar in decode(Image.open("temp.png")):
        if bar.data.decode("utf-8").upper().startswith(('420')):
            usps_tracking_number.append((bar.data.decode("utf-8")))
    os.remove("temp.png")
    try:
        if service == "Smart Label / Pitney Bowes":
            usps_tracking_number_input.insert(
                END, usps_tracking_number[0][-26:])
        elif service == "First Class Package Return":
            usps_tracking_number_input.insert(
                END, usps_tracking_number[0][-22:])
        elif service == "Priority Mail Return":
            usps_tracking_number_input.insert(
                END, usps_tracking_number[0][-22:])
        elif service == "UPS Mail Innovations":
            usps_tracking_number_input.insert(
                END, usps_tracking_number[0][-26:])
        elif service == "Smart Post":
            usps_tracking_number_input.insert(
                END, usps_tracking_number[0][-22:])
        elif service == "Ground Return Service":
            usps_tracking_number_input.insert(
                END, usps_tracking_number[0][-26:])
    except:
        uspsMessage("No tracking number found in document!")


def injectFileNameUSPS():
    basename = os.path.basename(usps_original_file_name)
    shortname, extension = os.path.splitext(basename)
    usps_file_name_input.insert(END, shortname + "_EDIT")


def selectOriginalLabelUPS():
    track_message.destroy()
    filetypes = (
        ('All files', '*.*'),
        ('png files', '*.png'),
        ('png files', '*.PNG'),
        ('pdf files', '*.PDF'),
        ('pdf files', '*.pdf'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg'),
        ('jpg files', '*.JPG'),
        ('jpg files', '*.JPEG'),
    )
    open1 = fd.askopenfilename(
        title='Open a file',
        initialdir=dir_path,
        filetypes=filetypes)
    global original_label_display
    if (open1):
        basename = os.path.basename(open1)
        shortname, extension = os.path.splitext(basename)
        original_label_display = tk.Label(
            ups_tab, text=shortname, font="arial 8")
        original_label_display.grid(row=1, column=1, sticky="w")
        global original_file_name
        original_file_name = open1
        collectTrackingNumberUPS(open1)
        injectFileNameUPS()
    else:
        upsMessage("File selection cancelled!")


def selectWeirdBarcodeUPS():
    track_message.destroy()
    filetypes = (
        ('All files', '*.*'),
        ('png files', '*.png'),
        ('png files', '*.PNG'),
        ('pdf files', '*.PDF'),
        ('pdf files', '*.pdf'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg'),
        ('jpg files', '*.JPG'),
        ('jpg files', '*.JPEG'),
    )
    open1 = fd.askopenfilename(
        title='Open a file',
        initialdir=dir_path,
        filetypes=filetypes)
    global selected_file_display
    if open1:
        basename = os.path.basename(open1)
        shortname, extension = os.path.splitext(basename)
        selected_file_display = tk.Label(
            ups_tab, text=shortname, font="arial 8")
        selected_file_display.grid(row=3, column=1, sticky="w")
        global file_name
        file_name = open1
    else:
        upsMessage("File selection cancelled!")


def injectFileNameUPS():
    basename = os.path.basename(original_file_name)
    shortname, extension = os.path.splitext(basename)
    file_name_input.insert(END, shortname + "_EDIT")


def collectTrackingNumberUPS(fileName):
    global tracking_number
    tracking_number = []
    file_name, file_extension = os.path.splitext(fileName)
    doc = fitz.open(fileName)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=150)
    pix.save("temp.png")
    for bar in decode(Image.open("temp.png")):
        if bar.data.decode("utf-8").upper().startswith(('1Z')):
            tracking_number.append((bar.data.decode("utf-8")))
    os.remove("temp.png")
    try:
        ups_tracking_number_input.insert(END, tracking_number[0])
        reverseTrackingLookup()
    except:
        upsMessage("No tracking number found in document!")


def upsOpenMaps():
    if len(ship_to_zip_input.get()) < 5:
        upsMessage("Enter a 5 digit zip code to open Google Maps!")
    else:
        webbrowser.open("http://maps.google.com/maps/search/" +
                        ship_to_zip_input.get())


def upsLit():
    global selected_file_display_2
    if (len(ups_lit.get()) < 1):
        selected_file_display_2.destroy()
        ups_region_input.configure(state="normal")
        weird_barcode_input.configure(state="normal")
        ups_region_input.delete(0, END)
        ups_scramble_tracking_box.configure(state="normal")
        ups_scramble_tracking.set(True)
        ups_return_address_box.configure(state="normal")
        upsMessage("LIT Mode Deactivated!")
    else:
        selected_file_display_2.destroy()
        selected_file_display_2 = tk.Label(
            ups_tab, text=ups_lit.get(), font="arial 8")
        selected_file_display_2.grid(row=3, column=1, sticky="w")
        ups_region_input.delete(0, END)
        new_region = str(random.randint(0, 9)) + "-" + \
            str(random.randint(10, 99))
        ups_region_input.insert(END, new_region)
        ups_region_input.configure(state="disabled")
        weird_barcode_input.configure(state="disabled")
        global file_name
        file_name = dir_path + "/resources/maxi/" + \
            str(random.randint(1, 8)) + ".png"
        ups_scramble_tracking.set(False)
        ups_scramble_tracking_box.configure(state="disabled")
        upsMessage("LIT Mode Activated!")


def upsEnableReturnAddressFields():
    if ups_return_address.get() == True:
        global ups_return_name_label
        global ups_return_name_input
        global ups_separator
        global ups_return_title
        global ups_return_address_label
        global ups_return_address_entry
        global ups_return_city_label
        global ups_return_city_entry
        global ups_return_state_label
        global ups_return_state_entry
        global ups_return_zip_label
        global ups_return_zip_entry
        global ups_return_generate_random_button
        global ups_return_clear
        ups_separator.destroy()
        ups_return_name_label.destroy()
        ups_return_name_input.destroy()
        ups_return_title.destroy()
        ups_return_title = tk.Label(
            ups_tab, text="Custom Return Address", font="arial 18")
        ups_return_title.grid(row=0, column=3, columnspan=2)
        ups_separator = ttk.Separator(ups_tab, orient=VERTICAL)
        ups_separator.grid(column=2, row=2, rowspan=20, sticky="ns", padx=10)
        ups_return_name_label = tk.Label(ups_tab, text="Name:")
        ups_return_name_label.grid(row=5, column=3, sticky="w")
        ups_return_name_input = tk.Entry(ups_tab, width=25)
        ups_return_name_input.grid(row=5, column=4, sticky="w")
        ups_return_address_label = tk.Label(ups_tab, text="Address:")
        ups_return_address_label.grid(row=6, column=3, sticky="w")
        ups_return_address_entry = tk.Entry(ups_tab, width=25)
        ups_return_address_entry.grid(row=6, column=4, sticky="w")
        ups_return_city_label = tk.Label(ups_tab, text="City:")
        ups_return_city_label.grid(row=7, column=3, sticky="w")
        ups_return_city_entry = tk.Entry(ups_tab, width=25)
        ups_return_city_entry.grid(row=7, column=4, sticky="w")
        ups_return_state_label = tk.Label(ups_tab, text="State:")
        ups_return_state_label.grid(row=8, column=3, sticky="w")
        ups_return_state_entry = tk.Entry(ups_tab, width=4)
        ups_return_state_entry.grid(row=8, column=4, sticky="w")
        ups_return_zip_label = tk.Label(ups_tab, text="Zip:")
        ups_return_zip_label.grid(row=9, column=3, sticky="w")
        ups_return_zip_entry = tk.Entry(ups_tab, width=6)
        ups_return_zip_entry.grid(row=9, column=4, sticky="w")
        ups_return_generate_random_button = tk.Button(
            ups_tab, text="Random Address", command=lambda: generateRandomAddress("ups"), fg="green")
        ups_return_generate_random_button.grid(row=14, column=4, sticky="w")
        ups_return_clear = tk.Button(
            ups_tab, text="Clear", command=upsReturnClear, fg="red")
        ups_return_clear.grid(row=14, column=3, sticky="w")
    else:
        ups_return_name_label.destroy()
        ups_return_name_input.destroy()
        ups_return_address_label.destroy()
        ups_return_address_entry.destroy()
        ups_return_city_label.destroy()
        ups_return_city_entry.destroy()
        ups_return_state_label.destroy()
        ups_return_state_entry.destroy()
        ups_return_zip_label.destroy()
        ups_return_zip_entry.destroy()
        ups_separator.destroy()
        ups_return_title.destroy()
        ups_return_generate_random_button.destroy()
        ups_return_clear.destroy()


def upsReturnClear():
    ups_return_name_input.delete(0, END)
    ups_return_address_entry.delete(0, END)
    ups_return_city_entry.delete(0, END)
    ups_return_state_entry.delete(0, END)
    ups_return_zip_entry.delete(0, END)


def selectOriginalLabelFedex():
    fedex_track_message.destroy()
    filetypes = (
        ('All files', '*.*'),
        ('png files', '*.png'),
        ('png files', '*.PNG'),
        ('pdf files', '*.PDF'),
        ('pdf files', '*.pdf'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg'),
        ('jpg files', '*.JPG'),
        ('jpg files', '*.JPEG'),
    )
    open1 = fd.askopenfilename(
        title='Open a file',
        initialdir=dir_path,
        filetypes=filetypes)
    global fedex_original_selected_file_display
    basename = os.path.basename(open1)
    shortname, extension = os.path.splitext(basename)
    if open1:
        fedex_original_selected_file_display = tk.Label(
            fedex_tab, text=shortname, font="arial 8")
        fedex_original_selected_file_display.grid(row=1, column=1, sticky="w")
        global fedex_original_file_name
        fedex_original_file_name = open1
        collectTrackingNumberFedex(open1)
        injectFileNameFedex()
    else:
        fedexMessage("File selection cancelled!")


def fedexSelectFile():  # weird
    fedex_track_message.destroy()
    filetypes = (
        ('All files', '*.*'),
        ('png files', '*.png'),
        ('png files', '*.PNG'),
        ('pdf files', '*.PDF'),
        ('pdf files', '*.pdf'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg'),
        ('jpg files', '*.JPG'),
        ('jpg files', '*.JPEG'),
    )
    open1 = fd.askopenfilename(
        title='Open a file',
        initialdir=dir_path,
        filetypes=filetypes)
    global fedex_selected_file_display
    basename = os.path.basename(open1)
    shortname, extension = os.path.splitext(basename)
    if open1:
        fedex_selected_file_display = tk.Label(
            fedex_tab, text=shortname, font="arial 8")
        fedex_selected_file_display.grid(row=3, column=1, sticky="w")
        global fedex_file_name
        fedex_file_name = open1
    else:
        fedexMessage("File selection cancelled!")


def injectFileNameFedex():
    basename = os.path.basename(fedex_original_file_name)
    shortname, extension = os.path.splitext(basename)
    fedex_file_name_input.insert(END, shortname + "_EDIT")


def collectTrackingNumberFedex(fileName):
    global fedex_tracking_number
    fedex_tracking_number = []
    file_name, file_extension = os.path.splitext(fileName)
    doc = fitz.open(fileName)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=150)
    pix.save("temp.png")
    for bar in decode(Image.open("temp.png")):
        if len(bar.data.decode("utf-8").upper()) > 21:
            fedex_tracking_number.append((bar.data.decode("utf-8")))
    os.remove("temp.png")
    try:
        fedex_tracking_number_input.insert(END, fedex_tracking_number[0])
    except:
        fedexMessage("No tracking number found in document!")


def fedexOpenMaps():
    if len(fedex_ship_to_zip_input.get()) < 5:
        fedexMessage("Enter a 5 digit zip code to open Google Maps!")
    else:
        webbrowser.open("http://maps.google.com/maps/search/" +
                        fedex_ship_to_zip_input.get())


def fedexLit():
    global selected_file_display_3
    if (len(fedex_lit.get()) < 1):
        selected_file_display_3.destroy()
        fedex_weird_barcode_input.configure(state="normal")
        fedex_express_button.configure(state="normal")
        fedex_Express.set(False)
        fedexMessage("LIT Mode Deactivated!")
    else:
        selected_file_display_3.destroy()
        selected_file_display_3 = tk.Label(
            fedex_tab, text=fedex_lit.get(), font="arial 8")
        selected_file_display_3.grid(row=3, column=1, sticky="w")
        fedex_weird_barcode_input.configure(state="disabled")
        global fedex_file_name
        fedex_file_name = dir_path + "/resources/pdf417/" + \
            str(random.randint(1, 8)) + ".png"
        fedex_Express.set(False)
        fedex_express_button.configure(state="disabled")
        fedexMessage("LIT Mode Activated!")


def fedexEnableReturnAddressFields():
    if fedex_return_address.get() == True:
        global fedex_return_name_label
        global fedex_return_name_input
        global fedex_separator
        global fedex_return_title
        global fedex_return_address_label
        global fedex_return_address_entry
        global fedex_return_city_label
        global fedex_return_city_entry
        global fedex_return_state_label
        global fedex_return_state_entry
        global fedex_return_zip_label
        global fedex_return_zip_entry
        global fedex_return_generate_random_button
        global fedex_return_clear
        fedex_separator.destroy()
        fedex_return_name_label.destroy()
        fedex_return_name_input.destroy()
        fedex_return_title.destroy()
        fedex_return_title = tk.Label(
            fedex_tab, text="Custom Return Address", font="arial 18")
        fedex_return_title.grid(row=0, column=3, columnspan=2)
        fedex_separator = ttk.Separator(fedex_tab, orient=VERTICAL)
        fedex_separator.grid(column=2, row=2, rowspan=20, sticky="ns", padx=10)
        fedex_return_name_label = tk.Label(fedex_tab, text="Name:")
        fedex_return_name_label.grid(row=5, column=3, sticky="w")
        fedex_return_name_input = tk.Entry(fedex_tab, width=25)
        fedex_return_name_input.grid(row=5, column=4, sticky="w")
        fedex_return_address_label = tk.Label(fedex_tab, text="Address:")
        fedex_return_address_label.grid(row=6, column=3, sticky="w")
        fedex_return_address_entry = tk.Entry(fedex_tab, width=25)
        fedex_return_address_entry.grid(row=6, column=4, sticky="w")
        fedex_return_city_label = tk.Label(fedex_tab, text="City:")
        fedex_return_city_label.grid(row=7, column=3, sticky="w")
        fedex_return_city_entry = tk.Entry(fedex_tab, width=25)
        fedex_return_city_entry.grid(row=7, column=4, sticky="w")
        fedex_return_state_label = tk.Label(fedex_tab, text="State:")
        fedex_return_state_label.grid(row=8, column=3, sticky="w")
        fedex_return_state_entry = tk.Entry(fedex_tab, width=4)
        fedex_return_state_entry.grid(row=8, column=4, sticky="w")
        fedex_return_zip_label = tk.Label(fedex_tab, text="Zip:")
        fedex_return_zip_label.grid(row=9, column=3, sticky="w")
        fedex_return_zip_entry = tk.Entry(fedex_tab, width=6)
        fedex_return_zip_entry.grid(row=9, column=4, sticky="w")
        fedex_return_generate_random_button = tk.Button(
            fedex_tab, text="Random Address", command=lambda: generateRandomAddress("fedex"), fg="green")
        fedex_return_generate_random_button.grid(row=13, column=4, sticky="w")
        fedex_return_clear = tk.Button(
            fedex_tab, text="Clear", command=fedexReturnClear, fg="red")
        fedex_return_clear.grid(row=13, column=3, sticky="w")
    else:
        fedex_return_name_label.destroy()
        fedex_return_name_input.destroy()
        fedex_return_address_label.destroy()
        fedex_return_address_entry.destroy()
        fedex_return_city_label.destroy()
        fedex_return_city_entry.destroy()
        fedex_return_state_label.destroy()
        fedex_return_state_entry.destroy()
        fedex_return_zip_label.destroy()
        fedex_return_zip_entry.destroy()
        fedex_separator.destroy()
        fedex_return_title.destroy()
        fedex_return_generate_random_button.destroy()
        fedex_return_clear.destroy()


def fedexReturnClear():
    fedex_return_name_input.delete(0, END)
    fedex_return_address_entry.delete(0, END)
    fedex_return_city_entry.delete(0, END)
    fedex_return_state_entry.delete(0, END)
    fedex_return_zip_entry.delete(0, END)


def generateRandomAddress(service):
    fake = Faker()
    fakeAddress = random_address.real_random_address()
    if service == "ups":
        upsReturnClear()
        try:
            ups_return_name_input.insert(END, fake.name().title())
            ups_return_address_entry.insert(END, fakeAddress['address1'])
            ups_return_city_entry.insert(END, fakeAddress['city'])
            ups_return_state_entry.insert(END, fakeAddress['state'])
            ups_return_zip_entry.insert(END, fakeAddress['postalCode'])
        except:
            generateRandomAddress(service)
    if service == "fedex":
        fedexReturnClear()
        try:
            fedex_return_name_input.insert(END, fake.name().title())
            fedex_return_address_entry.insert(END, fakeAddress['address1'])
            fedex_return_city_entry.insert(END, fakeAddress['city'])
            fedex_return_state_entry.insert(END, fakeAddress['state'])
            fedex_return_zip_entry.insert(END, fakeAddress['postalCode'])
        except:
            generateRandomAddress(service)


def upsMessage(message):
    global track_message
    track_message.destroy()
    track_message = tk.Label(ups_tab, text=message, font="arial 10")
    track_message.grid(row=30, column=1, sticky="e")

#do this last
def UPSvalidateFields():
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
              'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
              'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
              'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

    if len(ups_tracking_number_input.get()) < 1:
        upsMessage("Tracking number too short!")
        return False
    elif len(ship_to_name_input.get()) < 1:
        upsMessage("Please enter a ship to name!")
        return False
    elif len(ship_to_address1_input.get()) < 1:
        upsMessage("Please enter a ship to address!")
        return False
    elif len(ship_to_city_input.get()) < 1:
        upsMessage("Please enter a ship to city!")
        return False
    elif ship_to_state_input.get().upper() not in states:
        upsMessage("Not a valid state!")
        return False
    elif len(ship_to_zip_input.get()) < 5:
        upsMessage("Please enter a valid 5 digit zip code!")
        return False
    elif len(file_name_input.get()) < 1:
        upsMessage("Please enter a name for the output file!")
        return False
    elif (ups_return_address.get() == True) and len(ups_return_name_input.get()) < 1:
        upsMessage(
            "Please enter a return address name, or deselect Custom Return Address box!")
        return False
    elif (ups_return_address.get() == True) and len(ups_return_address_entry.get()) < 1:
        upsMessage(
            "Please enter a return address, or deselect Custom Return Address box!")
        return False
    elif (ups_return_address.get() == True) and len(ups_return_city_entry.get()) < 1:
        upsMessage(
            "Please enter a return address city, or deselect Custom Return Address box!")
        return False
    elif (ups_return_address.get() == True) and ups_return_state_entry.get().upper() not in states:
        upsMessage(
            "Please enter a valid return address state, or deselect Custom Return Address box!")
        return False
    elif (ups_return_address.get() == True) and len(ups_return_zip_entry.get()) < 1:
        upsMessage(
            "Please enter a return address zip, or deselect Custom Return Address box!")
        return False
    else:
        return True


def uspsMessage(message):
    global usps_track_message
    usps_track_message.destroy()
    usps_track_message = tk.Label(usps_tab, text=message, font="arial 10")
    usps_track_message.grid(row=30, column=1, sticky="e")


def fedexMessage(message):
    global fedex_track_message
    fedex_track_message.destroy()
    fedex_track_message = tk.Label(fedex_tab, text=message, font="arial 10")
    fedex_track_message.grid(row=30, column=1, sticky="e")


def fedexValidateFields():
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
              'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
              'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
              'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

    if len(fedex_tracking_number_input.get()) < 1:
        fedexMessage("Tracking number too short!")
        return False
    elif len(fedex_ship_to_name_input.get()) < 1:
        fedexMessage("Please enter a ship to name!")
        return False
    elif len(fedex_ship_to_address1_input.get()) < 1:
        fedexMessage("Please enter a ship to address!")
        return False
    elif len(fedex_ship_to_city_input.get()) < 1:
        fedexMessage("Please enter a ship to city!")
        return False
    elif fedex_ship_to_state_input.get().upper() not in states:
        fedexMessage("Not a valid state!")
        return False
    elif len(fedex_ship_to_zip_input.get()) < 5:
        fedexMessage("Please enter a valid 5 digit zip code!")
        return False
    elif len(fedex_file_name_input.get()) < 1:
        fedexMessage("Please enter a name for the output file!")
        return False
    elif (fedex_return_address.get() == True) and len(fedex_return_name_input.get()) < 1:
        fedexMessage(
            "Please enter a return address name, or deselect Custom Return Address box!")
        return False
    elif (fedex_return_address.get() == True) and len(fedex_return_address_entry.get()) < 1:
        fedexMessage(
            "Please enter a return address, or deselect Custom Return Address box!")
        return False
    elif (fedex_return_address.get() == True) and len(fedex_return_city_entry.get()) < 1:
        fedexMessage(
            "Please enter a return address city, or deselect Custom Return Address box!")
        return False
    elif (fedex_return_address.get() == True) and fedex_return_state_entry.get().upper() not in states:
        fedexMessage(
            "Please enter a valid return address state, or deselect Custom Return Address box!")
        return False
    elif (fedex_return_address.get() == True) and len(fedex_return_zip_entry.get()) < 1:
        fedexMessage(
            "Please enter a return address zip, or deselect Custom Return Address box!")
        return False
    else:
        return True


def UpsMainProgram():
    track_message.destroy()
    cont = UPSvalidateFields()
    if cont == False:
        return
    fake = Faker()
    blank_label = Image.open(dir_path + "/resources/master.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/DroidSans.ttf', 15)
    shipping_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/DroidSans.ttf', 25)
    shipping_address_city_font = ImageFont.truetype(
        dir_path + '/resources/fonts/DroidSans-Bold.ttf', 35)
    big_state_and_numbers_font = ImageFont.truetype(
        dir_path + '/resources/fonts/DroidSans-Bold.ttf', 66)
    big_h = ImageFont.truetype(
        dir_path + '/resources/fonts/DroidSans-Bold.ttf', 225)

    if ups_return_address.get() == True:
        return_text_name = ups_return_name_input.get().upper()
        return_text_address_1 = ups_return_address_entry.get().upper()
        return_text_address_2 = ups_return_city_entry.get().upper() + " " + \
            ups_return_state_entry.get().upper() + " " + ups_return_zip_entry.get().upper()
    else:
        try:
            return_text_name = fake.name().upper()
            new_random_address = random_address.real_random_address()
            return_text_address_1 = new_random_address['address1'].upper()
            return_text_address_2 = new_random_address['city'].upper(
            ) + " " + new_random_address['state'].upper() + " " + new_random_address['postalCode'].upper()
        except:
            return_text_name = fake.name().upper()
            new_random_address = random_address.real_random_address()
            return_text_address_1 = new_random_address['address1'].upper()
            return_text_address_2 = new_random_address['city'].upper(
            ) + " " + new_random_address['state'].upper() + " " + new_random_address['postalCode'].upper()
#stopped here
    ship_to_name = ship_to_name_input.get().upper()
    ship_to_address_1 = ship_to_address1_input.get().upper()
    ship_to_city = ship_to_city_input.get().upper()
    ship_to_state = ship_to_state_input.get().upper()
    ship_to_zip = ship_to_zip_input.get().upper()

    ship_to_address_2 = ship_to_city + " " + ship_to_state + " " + ship_to_zip

    if (len(ups_region_input.get()) < 4):
        ups_region = "9-01"
    else:
        ups_region = ups_region_input.get().upper()

    image_editable = ImageDraw.Draw(blank_label)

    tracking_number = ups_tracking_number_input.get()
    tracking_number = tracking_number.upper()
    tracking_number = tracking_number.replace(" ", "")
    tracking_number_with_spaces = tracking_number[:2] + " " + tracking_number[2:5] + " " + tracking_number[5:8] + \
        " " + tracking_number[8:10] + " " + \
        tracking_number[10:14] + " " + tracking_number[14:18]
    modified_tracking_number = tracking_number_with_spaces[:-9] + \
        tracking_number_with_spaces[19:] + tracking_number_with_spaces[13:18]

    big_barcode = code128.image(tracking_number, height=160)
    new_random_address2 = random_address.real_random_address()

    if (ups_lit.get() == "INJECTING FAKE MAXICODE FOR LIT"):
        tracking_number = "1Z" + random.choice(string.ascii_letters).upper() + str(random.randint(
            1, 9)) + random.choice(string.ascii_letters).upper() + str(random.randint(1000000000001, 9999999999999))
        tracking_number_with_spaces = tracking_number[:2] + " " + tracking_number[2:5] + " " + tracking_number[5:8] + \
            " " + tracking_number[8:10] + " " + \
            tracking_number[10:14] + " " + tracking_number[14:18]
        big_state_number = new_random_address2["state"].upper(
        ) + " " + str(random.randint(111, 999)) + "  " + ups_region
        small_barcode_text = "420" + str(random.randint(10001, 99999))
        small_barcode = code128.image(small_barcode_text, height=90)
    else:
        big_state_number = ship_to_state + " " + \
            ship_to_zip[0:3] + "  " + ups_region
        small_barcode_text = "420" + str(ship_to_zip)
        small_barcode = code128.image(small_barcode_text, height=90)

    # RETURN ADDRESS
    image_editable.text((15, 10), return_text_name,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 25), return_text_address_1,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 40), return_text_address_2,
                        (0, 0, 0), font=return_address_font)

    # SHIP TO ADDRESS
    image_editable.text((60, 135), ship_to_name, (0, 0, 0),
                        font=shipping_address_font)
    image_editable.text((60, 160), ship_to_address_1,
                        (0, 0, 0), font=shipping_address_font)
    image_editable.text((60, 185), ship_to_address_2,
                        (0, 0, 0), font=shipping_address_city_font)

    # TRACKING NUMBER
    if (ups_scramble_tracking.get() == True):
        image_editable.text((155, 583), modified_tracking_number,
                            (0, 0, 0), font=shipping_address_font)
    else:
        image_editable.text((155, 583), tracking_number_with_spaces,
                            (0, 0, 0), font=shipping_address_font)

    # STATE + 6 NUMBERS
    image_editable.text((220, 343), big_state_number,
                        (0, 0, 0), font=big_state_and_numbers_font)

    # SMALL BARCODE
    blank_label.paste(small_barcode, (230, 425))

    w, h = big_barcode.size
    big_barcode_cropped = big_barcode.crop((15, 0, w-10, h))
    big_barcode_resized = big_barcode_cropped.resize((490, 160))
    blank_label.paste(big_barcode_resized, (50, 645))

    if selected_file_display.winfo_exists():
        weird_file_name = file_name
        weird_barcode = Image.open(weird_file_name)
        blank_label.paste(weird_barcode.resize((177, 168)), (16, 350))
    else:
        if selected_file_display_2.winfo_exists():
            weird_file_name = file_name
            weird_barcode = Image.open(weird_file_name)
            blank_label.paste(weird_barcode.resize((177, 168)), (16, 350))
        else:
            image_editable.text((21, 308), "H", (0, 0, 0), font=big_h)

    blank_label.save(dir_path + "/modified_labels/" +
                     file_name_input.get() + ".png")

    # if selected_file_display.winfo_exists():
    #      os.remove(file_name)
    clear()

    upsMessage("Label generated successfully!")


def fedexMainProgram():
    fedex_track_message.destroy()
    cont = fedexValidateFields()
    if cont == False:
        return
    fake = Faker()

    if (fedex_Express.get() == True):
        blank_label = Image.open(
            dir_path + "/resources/master_fedex_express.png")
    elif (fedex_lit.get() == "INJECTING FAKE PDF417 FOR LIT"):
        blank_label = Image.open(
            dir_path + "/resources/master_fedex_express.png")
    else:
        blank_label = Image.open(dir_path + "/resources/master_fedex.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/Arial Narrow.ttf', 22)
    tracking_number_font = ImageFont.truetype(
        dir_path + '/resources/fonts/Arial Narrow.ttf', 36)
    tracking_number_font_smaller = ImageFont.truetype(
        dir_path + '/resources/fonts/Arial Narrow.ttf', 28)
    shipping_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/ArialNarrowBold.ttf', 30)
    zip_font = ImageFont.truetype(
        dir_path + '/resources/fonts/ArialNarrowBold.ttf', 45)
    cad_font = ImageFont.truetype(
        dir_path + '/resources/fonts/Arial Narrow.ttf', 20)

    if fedex_return_address.get() == True:
        return_text_name = fedex_return_name_input.get().title()
        return_text_address_1 = fedex_return_address_entry.get().title()
        return_text_address_2 = fedex_return_city_entry.get().title() + " " + \
            fedex_return_state_entry.get().upper() + " " + fedex_return_zip_entry.get().upper()
    else:
        try:
            return_text_name = fake.name().upper()
            new_random_address = random_address.real_random_address()
            return_text_address_1 = new_random_address['address1'].upper()
            return_text_address_2 = new_random_address['city'].upper(
            ) + " " + new_random_address['state'].upper() + " " + new_random_address['postalCode'].upper()
        except:
            return_text_name = fake.name().upper()
            new_random_address = random_address.real_random_address()
            return_text_address_1 = new_random_address['address1'].upper()
            return_text_address_2 = new_random_address['city'].upper(
            ) + " " + new_random_address['state'].upper() + " " + new_random_address['postalCode'].upper()

    ship_to_name = fedex_ship_to_name_input.get().title()
    ship_to_address_1 = fedex_ship_to_address1_input.get().title()
    ship_to_city = fedex_ship_to_city_input.get().title()
    ship_to_state = fedex_ship_to_state_input.get().upper()
    ship_to_zip = fedex_ship_to_zip_input.get().title()

    ship_to_address_2 = ship_to_city + " " + ship_to_state + " " + ship_to_zip

    cad_number = "CAD: " + \
        str(random.randint(111111111, 999999999)) + "/WSXI3100"

    fedex_tracking_number = fedex_tracking_number_input.get().upper()
    fedex_tracking_number = fedex_tracking_number.replace(" ", "")

    if len(fedex_tracking_number) < 28:
        modified_fedex_tracking_number = "(" + fedex_tracking_number[:7] + ") " + \
            fedex_tracking_number[14:24] + " " + fedex_tracking_number[7:14]
    else:
        modified_fedex_tracking_number = fedex_tracking_number[:4] + " " + fedex_tracking_number[4:8] + " " + fedex_tracking_number[8:9] + " (" + fedex_tracking_number[12:15] + " " + fedex_tracking_number[9:12] + " " + fedex_tracking_number[
            15:19] + ") " + fedex_tracking_number[19:20] + " " + fedex_tracking_number[20:22] + " " + fedex_tracking_number[22:26] + " " + fedex_tracking_number[30:34] + " " + fedex_tracking_number[26:30]

    modified_tracking_number = fedex_tracking_number[-12:-8] + " " + \
        fedex_tracking_number[-4:] + " " + fedex_tracking_number[-8:-4]

    random_phone_number = "(800)" + str(random.randint(111, 999)
                                        ) + "-" + str(random.randint(1111, 9999))

    PO_num = random.choice(string.ascii_uppercase) + \
        str(random.randint(111111111, 999999999))

    RMA_num = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + \
        random.choice(string.ascii_uppercase) + \
        str(random.randint(111111111111, 999999999999))
    RMA_barcode = code128.image(RMA_num, height=27)
    w, h = RMA_barcode.size
    RMA_barcode_cropped = RMA_barcode.crop((15, 0, w-10, h))

    big_barcode1 = code128.image(fedex_tracking_number, height=718)

    if len(fedex_tracking_number) < 28:
        big_barcode1 = big_barcode1.resize((725, 250))

    image_editable = ImageDraw.Draw(blank_label)

    # RETURN ADDRESS
    image_editable.text((250, 8), "(123) 456-7890",
                        (0, 0, 0), font=return_address_font)
    image_editable.text((38, 32), return_text_name,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((38, 68), return_text_address_1,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((38, 104), return_text_address_2,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((38, 124), "US", (0, 0, 0), font=return_address_font)

    # SHIP TO ADDRESS
    image_editable.text((44, 144), ship_to_name, (0, 0, 0),
                        font=shipping_address_font)
    image_editable.text((44, 224), ship_to_address_1,
                        (0, 0, 0), font=shipping_address_font)
    image_editable.text((44, 300), ship_to_address_2,
                        (0, 0, 0), font=shipping_address_font)
    image_editable.text((44, 334), random_phone_number,
                        (0, 0, 0), font=shipping_address_font)

    # TRACKING NUMBER
    image_editable.text((90, 775), modified_tracking_number,
                        (0, 0, 0), font=tracking_number_font)

    # Tracking Barcode
    blank_label.paste(big_barcode1, (80, 950))

    # SMALLER TRACKING NUMBER FULL
    if len(fedex_tracking_number) < 28:
        image_editable.text((255, 918), modified_fedex_tracking_number,
                            (0, 0, 0), font=tracking_number_font_smaller)
    else:
        image_editable.text((195, 918), modified_fedex_tracking_number,
                            (0, 0, 0), font=tracking_number_font_smaller)

    # Small RMA Barcode
    blank_label.paste(RMA_barcode_cropped, (75, 438))

    # CAD CODE
    image_editable.text((525, 50), cad_number, (0, 0, 0), font=cad_font)

    # RMA Code Upper
    image_editable.text((510, 379), RMA_num, (0, 0, 0), font=cad_font)

    # PO Number
    image_editable.text((75, 406), PO_num, (0, 0, 0), font=cad_font)

    # Zip Code
    if fedex_lit.get() == "INJECTING FAKE PDF417 FOR LIT":
        image_editable.text((710, 850), str(
            random.randint(10000, 99999)), (0, 0, 0), font=zip_font)
    else:
        image_editable.text((710, 850), ship_to_zip, (0, 0, 0), font=zip_font)

    # Weird Barcode
    if fedex_selected_file_display.winfo_exists():
        weird_file_name = fedex_file_name
        weird_barcode = Image.open(weird_file_name)
        blank_label.paste(weird_barcode.resize((633, 174)), (32, 475))
    else:
        if selected_file_display_3.winfo_exists():
            weird_file_name = fedex_file_name
            weird_barcode = Image.open(weird_file_name)
            blank_label.paste(weird_barcode.resize((633, 174)), (32, 475))
        else:
            weird_file_name = dir_path + "/resources/pdf417/" + \
                str(random.randint(1, 3)) + ".png"
            weird_barcode = Image.open(weird_file_name)
            blank_label.paste(weird_barcode.resize((633, 174)), (32, 475))

    file_name = fedex_file_name_input.get()
    blank_label.save(dir_path + "/modified_labels/" + file_name + ".png")

    clear()
    fedexMessage("Label generated successfully!")


def USPSSmartLabel():
    if len(usps_v_code_input.get()) < 1:
        uspsMessage("Please enter a mailer code!")
        return
    if len(usps_tracking_number_input.get()) < 1:
        uspsMessage("Please enter a tracking number!")
        return
    if len(usps_file_name_input.get()) < 1:
        uspsMessage("Please enter an output file name!")
        return
    fake = Faker()
    states = ['CA', 'CT', 'MA', 'VT', 'AL', 'AR', 'DC', 'FL',
              'GA', 'KY', 'MD', 'OK', 'TN', 'TX', 'AK', 'AZ', 'CO', 'HI']
    blank_label = Image.open(dir_path + "/resources/smartl_master.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 20)
    tracking_label_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSansBold.ttf', 25)
    v_code_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSansBold.ttf', 48)

    return_text_name = fake.name().upper()
    random_state = random.randint(0, 16)
    new_random_address = random_address.real_random_address_by_state(
        states[random_state])
    return_text_address_1 = new_random_address["address1"].upper()
    return_text_address_2 = new_random_address["city"].upper(
    ) + " " + new_random_address["state"].upper() + " " + new_random_address["postalCode"].upper()

    v_code = usps_v_code_input.get().upper()

    image_editable = ImageDraw.Draw(blank_label)

    rma_code = "72500" + str(new_random_address["postalCode"]) + "08" + str(
        random.randint(2000, 9999)) + "02" + str(random.randint(1000000000000, 9999999999999))
    rma_code_with_spaces = rma_code[:1] + " " + rma_code[1:3] + " " + rma_code[3:5] + " " + rma_code[5:10] + " " + rma_code[10:12] + \
        " " + rma_code[12:16] + " " + rma_code[16:17] + " " + \
        rma_code[18:19] + " " + rma_code[19:30] + " " + rma_code[30:]

    v_code = usps_v_code_input.get().upper()
    v_code_width = len(v_code)
    tracking_number = usps_tracking_number_input.get()
    tracking_number = tracking_number.upper()
    tracking_number_for_barcode = "(420)56901(92)" + tracking_number[2:]
    modified_tracking_number = tracking_number[:4] + " " + tracking_number[4:8] + " " + tracking_number[16:20] + " " + \
        tracking_number[8:12] + " " + tracking_number[12:16] + \
        " " + tracking_number[20:24] + " " + tracking_number[24:]

    big_barcode = treepoem.generate_barcode(
        barcode_type='gs1-128', data=tracking_number_for_barcode)
    other_barcode = treepoem.generate_barcode(
        barcode_type='code128', data=rma_code)

    # RETURN ADDRESS
    image_editable.text((15, 10), return_text_name,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 30), return_text_address_1,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 50), return_text_address_2,
                        (0, 0, 0), font=return_address_font)

    # TRACKING NUMBER
    image_editable.text((150, 835), modified_tracking_number,
                        (0, 0, 0), font=tracking_label_font)
    image_editable.text((75, 315), rma_code_with_spaces,
                        (0, 0, 0), font=return_address_font)

    big_barcode_resized = big_barcode.resize((610, 110))
    blank_label.paste(big_barcode_resized, (45, 685))

    other_barcode_resized = other_barcode.resize((480, 90))
    blank_label.paste(other_barcode_resized, (75, 220))

    image_editable.rectangle(
        (520, 915, (520+(v_code_width*31.25), 975)), fill='black')

    image_editable.text((525, 915), v_code, fill=(
        255, 255, 255), font=v_code_font)

    blank_label.save(dir_path + "/modified_labels/" +
                     usps_file_name_input.get() + ".png")

    clearSmartl()
    uspsMessage("Smart Label generated successfully!")


def USPSPriority():
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
              'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
              'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
              'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    if len(usps_ship_to_name_input.get()) < 1:
        uspsMessage("Please enter a ship to name!")
        return
    if len(usps_ship_to_address_input.get()) < 1:
        uspsMessage("Please enter a ship to address!")
        return
    if len(usps_ship_to_city_input.get()) < 1:
        uspsMessage("Please enter a ship to city!")
        return
    if usps_ship_to_state_input.get().upper() not in states:
        uspsMessage("Not a valid state!")
        return
    if len(usps_ship_to_zip_input.get()) < 1:
        uspsMessage("Please enter a valid 5 digit zip code!")
        return
    if len(usps_tracking_number_input.get()) < 1:
        uspsMessage("Please enter a tracking number!")
        return
    if len(usps_file_name_input.get()) < 1:
        uspsMessage("Please enter an output file name!")
        return
    fake = Faker()
    blank_label = Image.open(dir_path + "/resources/priority_master.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 20)
    tracking_label_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSansBold.ttf', 25)
    ship_to_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 30)

    return_text_name = fake.name()
    try:
        new_random_address = random_address.real_random_address()
        return_text_address_1 = new_random_address["address1"]
        return_text_address_2 = new_random_address["city"] + " " + \
            new_random_address["state"] + " " + \
            new_random_address["postalCode"]
    except:
        new_random_address = random_address.real_random_address()
        return_text_address_1 = new_random_address["address1"]
        return_text_address_2 = new_random_address["city"] + " " + \
            new_random_address["state"] + " " + \
            new_random_address["postalCode"]

    ship_to_name = usps_ship_to_name_input.get().title()
    ship_to_address = usps_ship_to_address_input.get().upper()
    ship_to_city = usps_ship_to_city_input.get().upper()
    ship_to_state = usps_ship_to_state_input.get().upper()
    ship_to_zip = usps_ship_to_zip_input.get().upper()
    ship_to_address_2 = ship_to_city + ", " + ship_to_state + " " + ship_to_zip

    image_editable = ImageDraw.Draw(blank_label)

    tracking_number = usps_tracking_number_input.get()
    tracking_number = tracking_number.upper()
    tracking_number_for_barcode = "(420)" + usps_ship_to_zip_input.get(
    ) + usps_ship_to_zip2_input.get() + "(92)" + tracking_number[2:]
    modified_tracking_number = tracking_number[:4] + " " + tracking_number[4:8] + " " + tracking_number[16:20] + \
        " " + tracking_number[8:12] + " " + \
        tracking_number[12:16] + " " + tracking_number[20:22]

    big_barcode = treepoem.generate_barcode(
        barcode_type='gs1-128', data=tracking_number_for_barcode)

    # RETURN ADDRESS
    image_editable.text((15, 280), return_text_name,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 300), return_text_address_1,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 320), return_text_address_2,
                        (0, 0, 0), font=return_address_font)

    # SHIP TO ADDRESS
    image_editable.text((125, 400), ship_to_name, (0, 0, 0), font=ship_to_font)
    image_editable.text((125, 430), ship_to_address,
                        (0, 0, 0), font=ship_to_font)
    image_editable.text((125, 460), ship_to_address_2,
                        (0, 0, 0), font=ship_to_font)

    # TRACKING NUMBER
    image_editable.text((165, 735), modified_tracking_number,
                        (0, 0, 0), font=tracking_label_font)

    big_barcode_resized = big_barcode.resize((610, 130))
    blank_label.paste(big_barcode_resized, (45, 590))

    blank_label.save(dir_path + "/modified_labels/" +
                     usps_file_name_input.get() + ".png")

    clearPri()
    uspsMessage("Priorty label generated successfully!")


def USPSSFirstClass():
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
              'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
              'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
              'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    if len(usps_ship_to_name_input.get()) < 1:
        uspsMessage("Please enter a ship to name!")
        return
    if len(usps_ship_to_address_input.get()) < 1:
        uspsMessage("Please enter a ship to address!")
        return
    if len(usps_ship_to_city_input.get()) < 1:
        uspsMessage("Please enter a ship to city!")
        return
    if usps_ship_to_state_input.get().upper() not in states:
        uspsMessage("Not a valid state!")
        return
    if len(usps_ship_to_zip_input.get()) < 1:
        uspsMessage("Please enter a valid 5 digit zip code!")
        return
    if len(usps_tracking_number_input.get()) < 1:
        uspsMessage("Please enter a tracking number!")
        return
    if len(usps_file_name_input.get()) < 1:
        uspsMessage("Please enter an output file name!")
        return
    fake = Faker()
    blank_label = Image.open(dir_path + "/resources/firstclass_master.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 20)
    tracking_label_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSansBold.ttf', 25)
    ship_to_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 30)

    return_text_name = fake.name()
    try:
        new_random_address = random_address.real_random_address()
        return_text_address_1 = new_random_address["address1"]
        return_text_address_2 = new_random_address["city"] + " " + \
            new_random_address["state"] + " " + \
            new_random_address["postalCode"]
    except:
        new_random_address = random_address.real_random_address()
        return_text_address_1 = new_random_address["address1"]
        return_text_address_2 = new_random_address["city"] + " " + \
            new_random_address["state"] + " " + \
            new_random_address["postalCode"]

    ship_to_name = usps_ship_to_name_input.get().title()
    ship_to_address = usps_ship_to_address_input.get().upper()
    ship_to_city = usps_ship_to_city_input.get().upper()
    ship_to_state = usps_ship_to_state_input.get().upper()
    ship_to_zip = usps_ship_to_zip_input.get().upper()
    ship_to_address_2 = ship_to_city + ", " + ship_to_state + " " + ship_to_zip

    image_editable = ImageDraw.Draw(blank_label)

    tracking_number = usps_tracking_number_input.get()
    tracking_number = tracking_number.upper()
    tracking_number_for_barcode = "(420)" + usps_ship_to_zip_input.get(
    ) + usps_ship_to_zip2_input.get() + "(92)" + tracking_number[2:]
    modified_tracking_number = tracking_number[:4] + " " + tracking_number[4:8] + " " + tracking_number[16:20] + \
        " " + tracking_number[8:12] + " " + \
        tracking_number[12:16] + " " + tracking_number[20:22]

    big_barcode = treepoem.generate_barcode(
        barcode_type='gs1-128', data=tracking_number_for_barcode)

    # RETURN ADDRESS
    image_editable.text((15, 280), return_text_name,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 300), return_text_address_1,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 320), return_text_address_2,
                        (0, 0, 0), font=return_address_font)

    # SHIP TO ADDRESS
    image_editable.text((125, 400), ship_to_name, (0, 0, 0), font=ship_to_font)
    image_editable.text((125, 430), ship_to_address,
                        (0, 0, 0), font=ship_to_font)
    image_editable.text((125, 460), ship_to_address_2,
                        (0, 0, 0), font=ship_to_font)

    # TRACKING NUMBER
    image_editable.text((165, 735), modified_tracking_number,
                        (0, 0, 0), font=tracking_label_font)

    big_barcode_resized = big_barcode.resize((610, 130))
    blank_label.paste(big_barcode_resized, (45, 590))

    blank_label.save(dir_path + "/modified_labels/" +
                     usps_file_name_input.get() + ".png")

    clearFc()
    uspsMessage("First Class Label generated successfully!")


def USPSSmartPost():
    if len(usps_tracking_number_input.get()) < 1:
        uspsMessage("Please enter a tracking number!")
        return
    if len(usps_file_name_input.get()) < 1:
        uspsMessage("Please enter an output file name!")
        return
    fake = Faker()
    blank_label = Image.open(dir_path + "/resources/smartp_master.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 20)
    tracking_label_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 22)

    ship_to_name = fake.name().title()
    try:
        new_random_address = random_address.real_random_address()
        ship_to_address = new_random_address["address1"].title()
        ship_to_address_2 = new_random_address["city"].title(
        ) + " " + new_random_address["state"].upper() + " " + new_random_address["postalCode"].upper()
    except:
        new_random_address = random_address.real_random_address()
        ship_to_address = new_random_address["address1"].title()
        ship_to_address_2 = new_random_address["city"].title(
        ) + " " + new_random_address["state"].upper() + " " + new_random_address["postalCode"].upper()

    image_editable = ImageDraw.Draw(blank_label)

    rma_code = str(random.randint(40000001, 90000001))

    tracking_number = usps_tracking_number_input.get()
    tracking_number = tracking_number.upper()
    tracking_number_for_barcode = "(420)56950(92)" + tracking_number[2:]
    modified_tracking_number = tracking_number[:4] + " " + tracking_number[4:8] + " " + tracking_number[16:20] + \
        " " + tracking_number[8:12] + " " + \
        tracking_number[12:16] + " " + tracking_number[20:22]

    big_barcode = treepoem.generate_barcode(
        barcode_type='gs1-128', data=tracking_number_for_barcode)
    other_barcode = treepoem.generate_barcode(
        barcode_type='code128', data=rma_code)

    # RETURN TO ADDRESS
    image_editable.text((70, 90), ship_to_name, (0, 0, 0),
                        font=return_address_font)
    image_editable.text((70, 110), ship_to_address,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((70, 130), ship_to_address_2,
                        (0, 0, 0), font=return_address_font)

    # TRACKING NUMBER
    image_editable.text((245, 793), modified_tracking_number,
                        (0, 0, 0), font=tracking_label_font)
    image_editable.text((90, 300), "RMA " + rma_code,
                        (0, 0, 0), font=return_address_font)

    big_barcode_resized = big_barcode.resize((565, 160))
    blank_label.paste(big_barcode_resized, (105, 625))

    other_barcode_resized = other_barcode.resize((200, 50))
    blank_label.paste(other_barcode_resized, (90, 250))

    blank_label.save(dir_path + "/modified_labels/" +
                     usps_file_name_input.get() + ".png")

    clearSmartp()
    uspsMessage("Smart Post Label generated successfully!")


def USPSMailInno():
    if len(usps_m_code_input.get()) < 1:
        uspsMessage(
            "Please enter the M Code found at the bottom of the original shipping label!")
        return
    if len(usps_tracking_number_input.get()) < 1:
        uspsMessage("Please enter a tracking number!")
        return
    if len(usps_file_name_input.get()) < 1:
        uspsMessage("Please enter an output file name!")
        return

    fake = Faker()
    blank_label = Image.open(dir_path + "/resources/mailinno_master.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/ArialNarrowBold.ttf', 20)
    m_code_font = ImageFont.truetype(
        dir_path + '/resources/fonts/ArialNarrowBold.ttf', 45)
    tracking_label_font = ImageFont.truetype(
        dir_path + '/resources/fonts/ArialNarrowBold.ttf', 28)

    return_address_name = fake.name().upper()

    try:
        new_random_address = random_address.real_random_address()
        return_address_1 = new_random_address["address1"].upper()
        return_address_2 = new_random_address["city"].upper(
        ) + " " + new_random_address["state"].upper() + " " + new_random_address["postalCode"].upper()
    except:
        new_random_address = random_address.real_random_address()
        return_address_1 = new_random_address["address1"].upper()
        return_address_2 = new_random_address["city"].upper(
        ) + " " + new_random_address["state"].upper() + " " + new_random_address["postalCode"].upper()

    m_code = usps_m_code_input.get()
    m_code = m_code.upper()
    image_editable = ImageDraw.Draw(blank_label)

    tracking_number = usps_tracking_number_input.get()
    tracking_number = tracking_number.upper()
    tracking_number_for_barcode = "(420)56935(92)" + tracking_number[2:]
    modified_tracking_number = tracking_number[:4] + " " + tracking_number[4:8] + " " + tracking_number[16:20] + " " + \
        tracking_number[8:12] + " " + tracking_number[12:16] + \
        " " + tracking_number[20:24] + " " + tracking_number[24:26]

    big_barcode = treepoem.generate_barcode(
        barcode_type='gs1-128', data=tracking_number_for_barcode)

    # RETURN TO ADDRESS
    image_editable.text((15, 10), return_address_name,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 30), return_address_1,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((15, 50), return_address_2,
                        (0, 0, 0), font=return_address_font)

    # MCODE
    image_editable.text((560, 690), m_code, (0, 0, 0), font=m_code_font)

    # TRACKING NUMBER
    image_editable.text((210, 455), modified_tracking_number,
                        (0, 0, 0), font=tracking_label_font)

    big_barcode_resized = big_barcode.resize((665, 160))
    blank_label.paste(big_barcode_resized, (50, 290))

    blank_label.save(dir_path + "/modified_labels/" +
                     usps_file_name_input.get() + ".png")

    clearMailInno()
    uspsMessage("UPS Mail Innovations label generated successfully!")


def USPSGround():
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
              'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
              'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
              'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    if len(usps_ship_to_name_input.get()) < 1:
        uspsMessage("Please enter a ship to name!")
        return
    if len(usps_ship_to_address_input.get()) < 1:
        uspsMessage("Please enter a ship to address!")
        return
    if len(usps_ship_to_city_input.get()) < 1:
        uspsMessage("Please enter a ship to city!")
        return
    if usps_ship_to_state_input.get().upper() not in states:
        uspsMessage("Not a valid state!")
        return
    if len(usps_ship_to_zip_input.get()) < 1:
        uspsMessage("Please enter a valid 5 digit zip code!")
        return
    if len(usps_tracking_number_input.get()) < 1:
        uspsMessage("Please enter a tracking number!")
        return
    if len(usps_file_name_input.get()) < 1:
        uspsMessage("Please enter an output file name!")
        return
    fake = Faker()
    blank_label = Image.open(dir_path + "/resources/ground_master.png")

    return_address_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 32)
    tracking_label_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSansBold.ttf', 34)
    ship_to_font = ImageFont.truetype(
        dir_path + '/resources/fonts/OpenSans.ttf', 38)

    return_text_name = fake.name().upper()
    try:
        new_random_address = random_address.real_random_address()
        return_text_address_1 = new_random_address["address1"].upper()
        return_text_address_2 = new_random_address["city"].upper(
        ) + " " + new_random_address["state"].upper() + " " + new_random_address["postalCode"].upper()
    except:
        new_random_address = random_address.real_random_address()
        return_text_address_1 = new_random_address["address1"].upper()
        return_text_address_2 = new_random_address["city"].upper(
        ) + " " + new_random_address["state"].upper() + " " + new_random_address["postalCode"].upper()

    ship_to_name = usps_ship_to_name_input.get().upper()
    ship_to_address = usps_ship_to_address_input.get().upper()
    ship_to_city = usps_ship_to_city_input.get().upper()
    ship_to_state = usps_ship_to_state_input.get().upper()
    ship_to_zip = usps_ship_to_zip_input.get().upper()
    ship_to_address_2 = ship_to_city + " " + ship_to_state + " " + ship_to_zip

    image_editable = ImageDraw.Draw(blank_label)

    tracking_number = usps_tracking_number_input.get()
    tracking_number = tracking_number.upper()
    tracking_number_for_barcode = "(420)" + \
        usps_ship_to_zip_input.get() + "(92)" + tracking_number[2:]
    modified_tracking_number = tracking_number[:4] + " " + tracking_number[4:8] + " " + tracking_number[16:20] + " " + \
        tracking_number[8:12] + " " + tracking_number[12:16] + \
        " " + tracking_number[20:24] + " " + tracking_number[24:26]

    big_barcode = treepoem.generate_barcode(
        barcode_type='gs1-128', data=tracking_number_for_barcode)

    # RETURN ADDRESS
    image_editable.text((25, 600), return_text_name,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((25, 632), return_text_address_1,
                        (0, 0, 0), font=return_address_font)
    image_editable.text((25, 664), return_text_address_2,
                        (0, 0, 0), font=return_address_font)

    # SHIP TO ADDRESS
    image_editable.text((150, 855), ship_to_name, (0, 0, 0), font=ship_to_font)
    image_editable.text((150, 893), ship_to_address,
                        (0, 0, 0), font=ship_to_font)
    image_editable.text((150, 931), ship_to_address_2,
                        (0, 0, 0), font=ship_to_font)

    # TRACKING NUMBER
    image_editable.text((275, 1525), modified_tracking_number,
                        (0, 0, 0), font=tracking_label_font)

    big_barcode_resized = big_barcode.resize((940, 200))
    blank_label.paste(big_barcode_resized, (75, 1300))

    blank_label.save(dir_path + "/modified_labels/" +
                     usps_file_name_input.get() + ".png")

    clearGround()
    uspsMessage("USPS Ground Label generated successfully!")


def clear():
    ups_region_input.configure(state="normal")
    weird_barcode_input.configure(state="normal")
    ship_to_state_input.configure(state="normal")
    ship_to_zip_input.configure(state="normal")
    ship_to_city_input.configure(state="normal")
    ups_tracking_number_input.configure(state="normal")
    ups_scramble_tracking_box.configure(state="normal")
    ship_to_name_input.delete(0, END)
    ship_to_address1_input.delete(0, END)
    ship_to_city_input.delete(0, END)
    ship_to_state_input.delete(0, END)
    ship_to_zip_input.delete(0, END)
    ups_region_input.delete(0, END)
    ups_tracking_number_input.delete(0, END)
    file_name_input.delete(0, END)
    selected_file_display.destroy()
    selected_file_display_2.destroy()
    original_label_display.destroy()
    track_message.destroy()
    ups_scramble_tracking.set(True)
    ups_lit.set(False)

    fedex_ship_to_name_input.delete(0, END)
    fedex_ship_to_address1_input.delete(0, END)
    fedex_ship_to_city_input.delete(0, END)
    fedex_ship_to_state_input.delete(0, END)
    fedex_ship_to_zip_input.delete(0, END)
    fedex_tracking_number_input.delete(0, END)
    fedex_file_name_input.delete(0, END)
    fedex_selected_file_display.destroy()
    fedex_original_selected_file_display.destroy()
    fedex_track_message.destroy()
    selected_file_display_3.destroy()
    fedex_file_name_input.configure(state="normal")
    fedex_express_button.configure(state="normal")
    fedex_weird_barcode_input.configure(state="normal")
    fedex_Express.set(False)
    fedex_lit.set(False)


def switchUsps():
    usps_v_code_label.destroy()
    usps_v_code_input.destroy()
    usps_m_code_label.destroy()
    usps_m_code_input.destroy()
    usps_ship_to_name_label.destroy()
    usps_ship_to_name_input.destroy()
    usps_ship_to_address_label.destroy()
    usps_ship_to_address_input.destroy()
    usps_ship_to_city_label.destroy()
    usps_ship_to_city_input.destroy()
    usps_ship_to_state_label.destroy()
    usps_ship_to_state_input.destroy()
    usps_ship_to_zip_label.destroy()
    usps_ship_to_zip_input.destroy()
    usps_ship_to_zip2_label.destroy()
    usps_ship_to_zip2_input.destroy()
    usps_tracking_number_label.destroy()
    usps_tracking_number_input.destroy()
    usps_file_name_label.destroy()
    usps_file_name_input.destroy()
    usps_createLabel.destroy()
    usps_resetForm.destroy()
    usps_original_label_label.destroy()
    usps_original_label_input.destroy()
    usps_original_display.destroy()
    usps_track_message.destroy()


def clearSmartl():
    usps_v_code_input.delete(0, END)
    usps_tracking_number_input.delete(0, END)
    usps_file_name_input.delete(0, END)
    usps_original_display.destroy()
    usps_track_message.destroy()


def clearGround():
    usps_ship_to_name_input.delete(0, END)
    usps_ship_to_address_input.delete(0, END)
    usps_ship_to_city_input.delete(0, END)
    usps_ship_to_state_input.delete(0, END)
    usps_ship_to_zip_input.delete(0, END)
    usps_tracking_number_input.delete(0, END)
    usps_tracking_number_input.delete(0, END)
    usps_file_name_input.delete(0, END)
    usps_file_name_input.delete(0, END)
    usps_original_display.destroy()
    usps_track_message.destroy()


def clearFc():
    usps_ship_to_name_input.delete(0, END)
    usps_ship_to_address_input.delete(0, END)
    usps_ship_to_city_input.delete(0, END)
    usps_ship_to_state_input.delete(0, END)
    usps_ship_to_zip_input.delete(0, END)
    usps_ship_to_zip2_input.delete(0, END)
    usps_tracking_number_input.delete(0, END)
    usps_file_name_input.delete(0, END)
    usps_original_display.destroy()
    usps_track_message.destroy()


def clearPri():
    usps_ship_to_name_input.delete(0, END)
    usps_ship_to_address_input.delete(0, END)
    usps_ship_to_city_input.delete(0, END)
    usps_ship_to_state_input.delete(0, END)
    usps_ship_to_zip_input.delete(0, END)
    usps_ship_to_zip2_input.delete(0, END)
    usps_tracking_number_input.delete(0, END)
    usps_file_name_input.delete(0, END)
    usps_original_display.destroy()
    usps_track_message.destroy()


def clearSmartp():
    usps_tracking_number_input.delete(0, END)
    usps_file_name_input.delete(0, END)
    usps_original_display.destroy()
    usps_track_message.destroy()


def clearMailInno():
    usps_m_code_input.delete(0, END)
    usps_tracking_number_input.delete(0, END)
    usps_file_name_input.delete(0, END)
    usps_original_display.destroy()
    usps_track_message.destroy()


def reverseTrackingLookup():
    tracking_number_to_lookup = ups_tracking_number_input.get().replace(" ", "")
    url = 'http://langley.one/ups/track?t=' + tracking_number_to_lookup
    track_message.destroy()
    try:
        x = requests.get(url)
        decoded_response = x.content.decode('utf-8')
        response_json = json.loads(json.dumps(
            xmltodict.parse(decoded_response)))
        parsed = json.dumps(response_json)
        json_parsed = json.loads(parsed)
        if json_parsed['TrackResponse']['Response']['ResponseStatusDescription'] == 'Success':
            ship_to_city_input.delete(0, END)
            ship_to_state_input.delete(0, END)
            ship_to_zip_input.delete(0, END)
            ups_tracking_number_input.delete(0, END)
            ship_to_state_input.insert(
                END, json_parsed['TrackResponse']['Shipment']['ShipTo']['Address']['StateProvinceCode'])
            ship_to_zip_input.insert(
                END, json_parsed['TrackResponse']['Shipment']['ShipTo']['Address']['PostalCode'])
            ship_to_city_input.insert(
                END, json_parsed['TrackResponse']['Shipment']['ShipTo']['Address']['City'])
            ups_tracking_number_input.insert(
                END, tracking_number_to_lookup.upper())
            ship_to_state_input.configure(state="disabled")
            ship_to_zip_input.configure(state="disabled")
            ship_to_city_input.configure(state="disabled")
            ups_tracking_number_input.configure(state="disabled")
        else:
            upsMessage("Tracking number invalid or not in UPS system yet!")
    except:
        upsMessage("Internet connection error!")

# Create the main window, and set the title
root = Tk()
root.title("Label Maker AiO v1.6")

# Create the tab widget
tabControl = ttk.Notebook(root)

ups_tab = ttk.Frame(tabControl)
fedex_tab = ttk.Frame(tabControl)
usps_tab = ttk.Frame(tabControl)

tabControl.add(ups_tab, text='UPS')
tabControl.add(fedex_tab, text='FedEx')
tabControl.add(usps_tab, text="USPS")
tabControl.pack(expand=1, fill="both")

######################################## return and ship to fields for ups tab ##################################
#done
original_label = tk.Label(ups_tab, text="Original Label: ")
original_label.grid(row=0, column=0, sticky="w")
original_label_input = tk.Button(
    ups_tab, text="select file", command=selectOriginalLabelUPS)
original_label_input.grid(row=0, column=1, sticky="w")
original_label_display = tk.Label(ups_tab)
original_label_display.destroy()
#done
weird_barcode_label = tk.Label(ups_tab, text="Maxicode Image: ")
weird_barcode_label.grid(row=2, column=0, sticky="w")
weird_barcode_input = tk.Button(
    ups_tab, text="select file", command=selectWeirdBarcodeUPS)
weird_barcode_input.grid(row=2, column=1, sticky="w")
selected_file_display = tk.Label(ups_tab)
selected_file_display.destroy()
#done
ship_to_name_label = tk.Label(ups_tab, text="Ship To Name: ")
ship_to_name_label.grid(row=5, column=0, sticky="w")
ship_to_name_input = tk.Entry(ups_tab, width=25)
ship_to_name_input.grid(row=5, column=1, sticky="w")
#done
ship_to_address1_label = tk.Label(ups_tab, text="Ship To Address: ")
ship_to_address1_label.grid(row=6, column=0, sticky="w")
ship_to_address1_input = tk.Entry(ups_tab, width=25)
ship_to_address1_input.grid(row=6, column=1, sticky="w")
ship_to_city_label = tk.Label(ups_tab, text="Ship To City: ")
ship_to_city_label.grid(row=7, column=0, sticky="w")
ship_to_city_input = tk.Entry(ups_tab, width=25)
ship_to_city_input.grid(row=7, column=1, sticky="w")
ship_to_state_label = tk.Label(ups_tab, text="Ship To State: ")
ship_to_state_label.grid(row=8, column=0, sticky="w")
ship_to_state_input = tk.Entry(ups_tab, width=4)
ship_to_state_input.grid(row=8, column=1, sticky="w")
ship_to_zip_label = tk.Label(ups_tab, text="Ship To Zip: ")
ship_to_zip_label.grid(row=9, column=0, sticky="w")
ship_to_zip_input = tk.Entry(ups_tab, width=7)
ship_to_zip_input.grid(row=9, column=1, sticky="w")
ups_region_label = tk.Label(ups_tab, text="UPS Region Code: ")
ups_region_label.grid(row=10, column=0, sticky="w")
ups_region_input = tk.Entry(ups_tab, width=7)
ups_region_input.grid(row=10, column=1, sticky="w")
ups_tracking_number_label = tk.Label(ups_tab, text="Tracking #: ")
ups_tracking_number_label.grid(row=11, column=0, sticky="w")
ups_tracking_number_input = tk.Entry(ups_tab, width=25)
ups_tracking_number_input.grid(row=11, column=1, sticky="w")
########################
file_name_label = tk.Label(ups_tab, text="Output File Name: ")
file_name_label.grid(row=12, column=0, sticky="w")
file_name_input = tk.Entry(ups_tab, width=25)
file_name_input.grid(row=12, column=1, sticky="w")
createLabel = tk.Button(ups_tab, text="Generate Label",
                        command=UpsMainProgram, fg="green")
createLabel.grid(row=14, column=1, sticky="w", pady=10)
######################
resetForm = tk.Button(ups_tab, text="Reset Form", command=clear, fg="red")
resetForm.grid(row=14, column=0, sticky="w", pady=10)
track_message = tk.Label(ups_tab)
track_message.destroy()
selected_file_display_2 = tk.Label(ups_tab)
selected_file_display_2.destroy()

ups_return_title = tk.Label(ups_tab)
ups_return_title.destroy()
ups_return_name_label = tk.Label(ups_tab)
ups_return_name_label.destroy()
ups_return_name_input = tk.Entry(ups_tab)
ups_return_name_input.destroy()
ups_separator = ttk.Separator(ups_tab)
ups_separator.destroy()
ups_return_address_label = tk.Label(ups_tab)
ups_return_address_label.destroy()
ups_return_address_entry = tk.Entry(ups_tab)
ups_return_address_entry.destroy()
ups_return_city_label = tk.Label(ups_tab)
ups_return_city_label.destroy()
ups_return_city_entry = tk.Entry(ups_tab)
ups_return_city_entry.destroy()
ups_return_state_label = tk.Label(ups_tab)
ups_return_state_label.destroy()
ups_return_state_entry = tk.Entry(ups_tab)
ups_return_state_entry.destroy()
ups_return_zip_label = tk.Label(ups_tab)
ups_return_zip_label.destroy()
ups_return_zip_entry = tk.Entry(ups_tab)
ups_return_zip_entry.destroy()
ups_return_generate_random_button = tk.Button(ups_tab)
ups_return_generate_random_button.destroy()
ups_return_clear = tk.Button(ups_tab)
ups_return_clear.destroy()

image1 = Image.open(dir_path + "/resources/maps_icon.png")
image2 = ImageTk.PhotoImage(image1)
find_a_business_button = tk.Button(
    ups_tab, image=image2, command=upsOpenMaps)
find_a_business_button.grid(row=9, column=0, sticky="e")

imageGlass = Image.open(dir_path + "/resources/glass.png")
imageGlass2 = ImageTk.PhotoImage(imageGlass)
tracking_lookup_button = tk.Button(
    ups_tab, image=imageGlass2, command=reverseTrackingLookup)
tracking_lookup_button.grid(row=11, column=0, sticky="e")

ups_scramble_tracking = tk.BooleanVar(value=True)
ups_scramble_tracking_box = tk.Checkbutton(
    ups_tab, text="Scramble Tracking Number Shown on Label?", font="arial 10", variable=ups_scramble_tracking)
ups_scramble_tracking_box.grid(
    row=19, column=0, columnspan=2, sticky="w", pady=10)

ups_return_address = tk.BooleanVar(value=False)
ups_return_address_box = tk.Checkbutton(ups_tab, text="Custom Return Address?", command=upsEnableReturnAddressFields,
                                        onvalue=True, offvalue=False, font="arial 10", variable=ups_return_address)
ups_return_address_box.grid(row=18, column=1, sticky="w")

ups_lit = tk.StringVar(value=False)
ups_lit_box = tk.Checkbutton(ups_tab, text="LIT Mode", font="arial 10", command=upsLit,
                                variable=ups_lit, onvalue="INJECTING FAKE MAXICODE FOR LIT", offvalue="")
ups_lit_box.grid(row=18, column=0, sticky="w", pady=10)

######################################## return and ship to fields for fedex tab########################################

fedex_original_label = tk.Label(fedex_tab, text="Original Label: ")
fedex_original_label.grid(row=0, column=0, sticky="w")
fedex_original_label_input = tk.Button(
    fedex_tab, text="select file", command=selectOriginalLabelFedex)
fedex_original_label_input.grid(row=0, column=1, sticky="w")
fedex_original_selected_file_display = tk.Label(fedex_tab)
fedex_original_selected_file_display.destroy()

fedex_weird_barcode_label = tk.Label(fedex_tab, text="pdf417 Barcode: ")
fedex_weird_barcode_label.grid(row=2, column=0, sticky="w")
fedex_weird_barcode_input = tk.Button(
    fedex_tab, text="select file", command=fedexSelectFile)
fedex_weird_barcode_input.grid(row=2, column=1, sticky="w")
fedex_selected_file_display = tk.Label(fedex_tab)
fedex_selected_file_display.destroy()

fedex_ship_to_name_label = tk.Label(fedex_tab, text="Ship To Name: ")
fedex_ship_to_name_label.grid(row=5, column=0, sticky="w")
fedex_ship_to_name_input = tk.Entry(fedex_tab, width=25)
fedex_ship_to_name_input.grid(row=5, column=1, sticky="w")
fedex_ship_to_address1_label = tk.Label(
    fedex_tab, text="Ship To Address: ")
fedex_ship_to_address1_label.grid(row=6, column=0, sticky="w")
fedex_ship_to_address1_input = tk.Entry(fedex_tab, width=25)
fedex_ship_to_address1_input.grid(row=6, column=1, sticky="w")
fedex_ship_to_city_label = tk.Label(fedex_tab, text="Ship To City: ")
fedex_ship_to_city_label.grid(row=7, column=0, sticky="w")
fedex_ship_to_city_input = tk.Entry(fedex_tab, width=25)
fedex_ship_to_city_input.grid(row=7, column=1, sticky="w")
fedex_ship_to_state_label = tk.Label(fedex_tab, text="Ship To State: ")
fedex_ship_to_state_label.grid(row=8, column=0, sticky="w")
fedex_ship_to_state_input = tk.Entry(fedex_tab, width=4)
fedex_ship_to_state_input.grid(row=8, column=1, sticky="w")
fedex_ship_to_zip_label = tk.Label(fedex_tab, text="Ship To Zip: ")
fedex_ship_to_zip_label.grid(row=9, column=0, sticky="w")
fedex_ship_to_zip_input = tk.Entry(fedex_tab, width=7)
fedex_ship_to_zip_input.grid(row=9, column=1, sticky="w")
fedex_tracking_number_label = tk.Label(fedex_tab, text="Tracking #: ")
fedex_tracking_number_label.grid(row=10, column=0, sticky="w")
fedex_tracking_number_input = tk.Entry(fedex_tab, width=25)
fedex_tracking_number_input.grid(row=10, column=1, sticky="w")

fedex_file_name_label = tk.Label(fedex_tab, text="Output File Name: ")
fedex_file_name_label.grid(row=11, column=0, sticky="w")
fedex_file_name_input = tk.Entry(fedex_tab, width=25)
fedex_file_name_input.grid(row=11, column=1, sticky="w")
fedex_createLabel = tk.Button(
    fedex_tab, text="Generate Label", command=fedexMainProgram, fg="green")
fedex_createLabel.grid(row=13, column=1, sticky="w", pady=10)
fedex_resetForm = tk.Button(
    fedex_tab, text="Reset Form", command=clear, fg="red")
fedex_resetForm.grid(row=13, column=0, sticky="w", pady=10)
fedex_track_message = tk.Label(fedex_tab)
fedex_track_message.destroy()

selected_file_display_3 = tk.Label(fedex_tab)
selected_file_display_3.destroy()

fedex_Express = tk.BooleanVar(value=False)
fedex_express_button = tk.Checkbutton(
    fedex_tab, text="Fedex Express", font="arial 10", variable=fedex_Express)
fedex_express_button.grid(row=16, column=0, sticky="w", pady=10)

image3 = Image.open(dir_path + "/resources/maps_icon.png")
image4 = ImageTk.PhotoImage(image3)
fedex_find_a_business_label = tk.Label(text="Open Maps", image=image2)
fedex_find_a_business_button = tk.Button(
    fedex_tab, image=image2, command=fedexOpenMaps)
fedex_find_a_business_button.grid(row=9, column=0, sticky="e")

fedex_lit = tk.StringVar(value=False)
fedex_lit_box = tk.Checkbutton(fedex_tab, text="LIT Mode", font="arial 10", command=fedexLit,
                                variable=fedex_lit, onvalue="INJECTING FAKE PDF417 FOR LIT", offvalue="")
fedex_lit_box.grid(row=15, column=0, columnspan=2, sticky="w", pady=10)

fedex_return_title = tk.Label(fedex_tab)
fedex_return_title.destroy()
fedex_return_name_label = tk.Label(fedex_tab)
fedex_return_name_label.destroy()
fedex_return_name_input = tk.Entry(fedex_tab)
fedex_return_name_input.destroy()
fedex_separator = ttk.Separator(fedex_tab)
fedex_separator.destroy()
fedex_return_address_label = tk.Label(fedex_tab)
fedex_return_address_label.destroy()
fedex_return_address_entry = tk.Entry(fedex_tab)
fedex_return_address_entry.destroy()
fedex_return_city_label = tk.Label(fedex_tab)
fedex_return_city_label.destroy()
fedex_return_city_entry = tk.Entry(fedex_tab)
fedex_return_city_entry.destroy()
fedex_return_state_label = tk.Label(fedex_tab)
fedex_return_state_label.destroy()
fedex_return_state_entry = tk.Entry(fedex_tab)
fedex_return_state_entry.destroy()
fedex_return_zip_label = tk.Label(fedex_tab)
fedex_return_zip_label.destroy()
fedex_return_zip_entry = tk.Entry(fedex_tab)
fedex_return_zip_entry.destroy()
fedex_return_generate_random_button = tk.Button(fedex_tab)
fedex_return_generate_random_button.destroy
fedex_return_clear = tk.Button(fedex_tab)
fedex_return_clear.destroy()

fedex_return_address = tk.BooleanVar(value=False)
fedex_return_address_box = tk.Checkbutton(fedex_tab, text="Custom Return Address?", command=fedexEnableReturnAddressFields,
                                            onvalue=True, offvalue=False, font="arial 10", variable=fedex_return_address)
fedex_return_address_box.grid(row=15, column=1, sticky="w")
#########################################################################################################################
# USPS TAB#

usps_drop_down_options = ["Smart Label / Pitney Bowes", "First Class Package Return",
                            "Priority Mail Return", "Smart Post", "UPS Mail Innovations", "Ground Return Service"]
usps_drop_down_clicked = StringVar()
usps_drop_down_clicked.set("Select a Label Template")
usps_drop_down_menu = OptionMenu(
    usps_tab, usps_drop_down_clicked, *usps_drop_down_options)
usps_drop_down_menu.grid(row=0, column=0, sticky="", columnspan=2, pady=10)
usps_drop_down_clicked.trace("w", uspsSetup)

usps_original_label_label = tk.Label(usps_tab)
usps_original_label_label.destroy()
usps_original_label_input = tk.Button(usps_tab)
usps_original_label_input.destroy()
usps_original_display = tk.Label(usps_tab)
usps_original_display.destroy()

usps_tracking_number_label = tk.Label(usps_tab)
usps_tracking_number_label.destroy()
usps_tracking_number_input = tk.Entry(usps_tab)
usps_tracking_number_input.destroy()

usps_from_state_label = tk.Label(usps_tab)
usps_from_state_label.destroy()
usps_from_state_input = tk.Entry(usps_tab)
usps_from_state_input.destroy()
usps_v_code_label = tk.Label(usps_tab)
usps_v_code_label.destroy()
usps_v_code_input = tk.Entry(usps_tab)
usps_v_code_input.destroy()
usps_ship_to_name_label = tk.Label(usps_tab)
usps_ship_to_name_label.destroy()
usps_ship_to_name_input = tk.Entry(usps_tab)
usps_ship_to_name_input.destroy()
usps_ship_to_address_label = tk.Label(usps_tab)
usps_ship_to_address_label.destroy()
usps_ship_to_address_input = tk.Entry(usps_tab)
usps_ship_to_address_input.destroy()
usps_ship_to_city_label = tk.Label(usps_tab)
usps_ship_to_city_label.destroy()
usps_ship_to_city_input = tk.Entry(usps_tab)
usps_ship_to_city_input.destroy()
usps_ship_to_state_label = tk.Label(usps_tab)
usps_ship_to_state_label.destroy()
usps_ship_to_state_input = tk.Entry(usps_tab)
usps_ship_to_state_input.destroy()
usps_ship_to_zip_label = tk.Label(usps_tab)
usps_ship_to_zip_label.destroy()
usps_ship_to_zip_input = tk.Entry(usps_tab)
usps_ship_to_zip_input.destroy()
usps_ship_to_zip2_label = tk.Label(usps_tab)
usps_ship_to_zip2_label.destroy()
usps_ship_to_zip2_input = tk.Entry(usps_tab)
usps_ship_to_zip2_input.destroy()
usps_m_code_label = tk.Label(usps_tab)
usps_m_code_label.destroy()
usps_m_code_input = tk.Entry(usps_tab)
usps_m_code_input.destroy()
usps_file_name_label = tk.Label(usps_tab)
usps_file_name_label.destroy()
usps_file_name_input = tk.Entry(usps_tab)
usps_file_name_input.destroy()
usps_createLabel = tk.Button(usps_tab)
usps_createLabel.destroy()
usps_resetForm = tk.Button(usps_tab)
usps_resetForm.destroy()

usps_track_message = tk.Label(usps_tab)
usps_track_message.destroy()

root.mainloop()
