from cmath import exp
from operator import index
import pandas as pd
from tkinter import*
from tkinter import ttk, filedialog
from tkinter.font import BOLD
from tkcalendar import Calendar
import datetime
# from datetime import date
# import random
# import time
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
import os
from sqlalchemy import create_engine


class homePage():
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1540x800+0+0")

        self.username = StringVar()
        self.password = StringVar()

        # self.varIndentNo = StringVar()
        # self.varItemDesc = StringVar()
        # self.varDivision = StringVar()
        # self.varIndentorName = StringVar()
        # self.varModeOfProc = StringVar()
        # # self.varSpecs = StringVar()
        # self.varAmountEstimate = DoubleVar()
        # self.varStatus = StringVar()
        # self.varActualAmount = DoubleVar()
        # self.varAdditionalInfo = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="LOGIN",
                         fg="red", bg="white", font=("times new roman", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        dataFrame = Frame(self.root)
        dataFrame.pack(fill=BOTH, expand=True, padx=10, pady=(50, 10))

        recordFrame1 = Frame(dataFrame)
        recordFrame1.pack(side=LEFT, fill=BOTH, expand=True,
                          padx=(10, 5), pady=(10, 0))

        recordFrame2 = Frame(dataFrame)
        recordFrame2.pack(side=LEFT, fill=BOTH,
                          expand=True, padx=(5, 10), pady=(10, 0))

        recordFrame3 = Frame(self.root)
        recordFrame3.pack(side=TOP, fill=BOTH,
                          expand=True, padx=(5, 10), pady=(0, 10))

        lblUsername = Label(
            recordFrame1, text="Username :", font=("arial", 20, "bold"))
        lblUsername.pack(side=TOP,
                         expand=True)

        lblNamePassword = Label(
            recordFrame1, text="Password :", font=("arial", 20, "bold"))
        lblNamePassword.pack(side=TOP,
                             expand=True)

        entryNameUsername = Entry(
            recordFrame2, textvariable=self.username, font=("arial", 20, "bold"))
        entryNameUsername.pack(side=TOP,
                               expand=True)

        entryNamePassword = Entry(
            recordFrame2, textvariable=self.password, font=("arial", 20, "bold"), show="*")
        entryNamePassword.pack(side=TOP,
                               expand=True)

        self.btnNameHomePage = Button(recordFrame3, text="Login", font=(
            "arial", 20, "bold"), command=self.funcHomePageAuthenticate)
        self.btnNameHomePage.pack(side=TOP,
                                  expand=True)

    def funcHomePageAuthenticate(self):
        if (self.username.get() == "admin" and self.password.get() == "1234"):
            self.funcHomePage()

    def funcHomePage(self):
        self.username = StringVar()
        self.password = StringVar()
        self.btnNameHomePage.config(command="")
        self.homePageTopLevel = Toplevel(self.root)
        self.homePageTopLevel.geometry("1540x800+0+0")
        self.homePageTopLevel.title("HOME")

        lbltitle = Label(self.homePageTopLevel, bd=20, relief=RIDGE, text="INVENTORY MANAGEMENT SYSTEM",
                         fg="red", bg="white", font=("times new roman", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        dataFrame = Frame(self.homePageTopLevel)
        dataFrame.pack(fill=BOTH, expand=True, padx=10, pady=(50, 10))

        recordFrame1 = Frame(dataFrame)
        recordFrame1.pack(side=LEFT, fill=BOTH, expand=True,
                          padx=(10, 5), pady=(10, 0))

        # recordFrame2 = Frame(dataFrame)
        # recordFrame2.pack(side=LEFT, fill=BOTH,
        #                   expand=True, padx=(5, 10), pady=(10, 0))

        recordFrame3 = Frame(self.homePageTopLevel)
        recordFrame3.pack(side=TOP, fill=BOTH,
                          expand=True, padx=(5, 10), pady=(0, 10))

        self.btnNameNewRecord = Button(
            recordFrame1, text="NEW RECORD", font=("arial", 20, "bold"), command=self.funcNewRecord)
        self.btnNameNewRecord.pack(side=TOP,
                                   expand=True)

        self.btnNameUpdateRecord = Button(
            recordFrame1, text="UPDATE RECORD", font=("arial", 20, "bold"), command=self.funcUpdateRecord)
        self.btnNameUpdateRecord.pack(side=TOP,
                                      expand=True)

        # self.btnNameSearchRecord = Button(
        #     recordFrame2, text="SEARCH RECORD", font=("arial", 20, "bold"), command=self.funcSearchRecord)
        # self.btnNameSearchRecord.pack(side=TOP,
        #                               expand=True)

        # self.btnNameDeleteRecord = Button(
        #     recordFrame2, text="DELETE RECORD", font=("arial", 20, "bold"), command=self.funcDeleteRecord)
        # self.btnNameDeleteRecord.pack(side=TOP,
        #                               expand=True)

        self.btnNameUploadCSVRecord = Button(
            recordFrame3, text="INSERT MULTIPLE RECORDS", font=("arial", 20, "bold"), command=self.funcUploadCSVFile)
        self.btnNameUploadCSVRecord.pack(side=TOP,
                                         expand=True)

        def quit_window():
            self.btnNameHomePage.config(command=self.funcHomePage)
            self.homePageTopLevel.destroy()

        self.homePageTopLevel.protocol("WM_DELETE_WINDOW", quit_window)

    def funcNewRecord(self):
        self.btnNameNewRecord.config(command="")

        self.newRecordTopLevel = Toplevel(self.root)
        self.newRecordTopLevel.geometry("1540x800+0+0")
        self.newRecordTopLevel.title("NEW RECORD")

        self.varIndentNo = StringVar()
        self.varItemDesc = StringVar()
        self.varDivision = StringVar()
        self.varIndentorName = StringVar()
        self.varModeOfProc = StringVar()
        self.varAmountEstimate = DoubleVar()
        self.varStatus = StringVar()
        self.varActualAmount = DoubleVar()
        self.varAdditionalInfo = StringVar()
        self.uploadSpecsBinaryData = ""
        self.varDateRaised = ""
        self.varDeliveryDateShow = ""

        lbltitle = Label(self.newRecordTopLevel, bd=20, relief=RIDGE, text="NEW RECORD",
                         fg="red", bg="white", font=("times new roman", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        dataFrame = LabelFrame(self.newRecordTopLevel, bd=20, relief=RIDGE, font=(
            "arial", 30, "bold"), text="ENTER NEW RECORD DETAILS")
        dataFrame.pack(fill=BOTH, expand=True, padx=10, pady=(20, 10))

        self.newRecordFrame1 = Frame(dataFrame, bd=20, relief=RIDGE)
        self.newRecordFrame1.pack(side=LEFT, fill=BOTH, expand=True,
                                  padx=(10, 5), pady=(10, 10))

        newRecordFrame2 = Frame(dataFrame, bd=20, relief=RIDGE)
        newRecordFrame2.pack(side=LEFT, fill=BOTH,
                             expand=True, padx=(5, 10), pady=(10, 10))

        newRecordFrame3 = Frame(self.newRecordTopLevel, bd=20, relief=RIDGE)
        newRecordFrame3.pack(fill=BOTH,
                             expand=True, padx=(10, 10), pady=(0, 10))

        lblNameIndent = Label(
            self.newRecordFrame1, text="INDENT NO", font=("arial", 20, "bold"))
        lblNameIndent.grid(row=0, column=0, sticky=W)

        newRecordentryNameIndent = Entry(
            self.newRecordFrame1, font=("arial", 20, "bold"), textvariable=self.varIndentNo)
        newRecordentryNameIndent.grid(row=0, column=1, sticky=E)

        lblNameDateRaised = Label(
            self.newRecordFrame1, text="DATE RAISED", font=("arial", 20, "bold"))
        lblNameDateRaised.grid(row=1, column=0, sticky=W)

        btnNameDateRaised = Button(self.newRecordFrame1, text="SELECT", font=(
            "arial", 10, "bold"), command=self.funcNewRecordDateRaised)
        btnNameDateRaised.grid(row=1, column=2, padx=20)

        lblNameItemDesc = Label(
            self.newRecordFrame1, text="ITEM DESCRP", font=("arial", 20, "bold"))
        lblNameItemDesc.grid(row=2, column=0, sticky=W)

        newRecordentryNameItemDesc = Entry(
            self.newRecordFrame1, font=("arial", 20, "bold"), textvariable=self.varItemDesc)
        newRecordentryNameItemDesc.grid(row=2, column=1, sticky=E)

        lblNameDivName = Label(
            self.newRecordFrame1, text="DIVISION", font=("arial", 20, "bold"))
        lblNameDivName.grid(row=3, column=0, sticky=W)

        newRecordentryNameDivName = Entry(
            self.newRecordFrame1, font=("arial", 20, "bold"), textvariable=self.varDivision)
        newRecordentryNameDivName.grid(row=3, column=1, sticky=E)

        lblNameIndentorName = Label(
            self.newRecordFrame1, text="INDENTOR NAME", font=("arial", 20, "bold"))
        lblNameIndentorName.grid(row=4, column=0, sticky=W)

        newRecordentryNameIndentorName = Entry(
            self.newRecordFrame1, font=("arial", 20, "bold"), textvariable=self.varIndentorName)
        newRecordentryNameIndentorName.grid(row=4, column=1, sticky=E)

        lblNameDeliveryDate = Label(
            self.newRecordFrame1, text="DELIVERY DATE", font=("arial", 20, "bold"))
        lblNameDeliveryDate.grid(row=5, column=0, sticky=W)

        btnNameDeliveryDate = Button(self.newRecordFrame1, text="SELECT", font=(
            "arial", 10, "bold"), command=self.funcNewRecordDeliveryDate)
        btnNameDeliveryDate.grid(row=5, column=2, padx=20)

        lblNameModeOfProc = Label(
            newRecordFrame2, text="MODE OF PROCUREMENT", font=("arial", 20, "bold"))
        lblNameModeOfProc.grid(row=0, column=0, sticky=W)

        newRecordcomboboxNameModeOfProc = ttk.Combobox(
            newRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varModeOfProc)
        newRecordcomboboxNameModeOfProc.grid(row=0, column=1, sticky=E)

        newRecordcomboboxNameModeOfProc['value'] = (
            "SELECT", "GEM", "OPEN TENDER", "LIMITED TENDER")

        newRecordcomboboxNameModeOfProc.current(0)

        lblNameSpecs = Label(
            newRecordFrame2, text="SPECS", font=("arial", 20, "bold"))
        lblNameSpecs.grid(row=1, column=0, sticky=W)

        self.btnNameUploadSpecs = Button(newRecordFrame2, text="UPLOAD FILE", font=(
            "arial", 10, "bold"), command=self.funcNewRecordUploadSpecsFileFirst)
        self.btnNameUploadSpecs.grid(row=1, column=1)

        lblNameAmountEstimate = Label(
            newRecordFrame2, text="AMOUNT ESTIMATE", font=("arial", 20, "bold"))
        lblNameAmountEstimate.grid(row=2, column=0, sticky=W)

        newRecordentryNameAmountEstimate = Entry(
            newRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varAmountEstimate)
        newRecordentryNameAmountEstimate.grid(row=2, column=1, sticky=E)

        lblNameStatus = Label(
            newRecordFrame2, text="STATUS", font=("arial", 20, "bold"))
        lblNameStatus.grid(row=3, column=0, sticky=W)

        newRecordentryNameStatus = Entry(
            newRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varStatus)
        newRecordentryNameStatus.grid(row=3, column=1, sticky=E)

        lblNameActualAmount = Label(
            newRecordFrame2, text="ACTUAL AMOUNT", font=("arial", 20, "bold"))
        lblNameActualAmount.grid(row=4, column=0, sticky=W)

        newRecordentryNameActualAmount = Entry(
            newRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varActualAmount)
        newRecordentryNameActualAmount.grid(row=4, column=1, sticky=E)

        lblNameAdditionalInfo = Label(
            newRecordFrame2, text="ADDITIONAL INFO", font=("arial", 20, "bold"))
        lblNameAdditionalInfo.grid(row=5, column=0, sticky=W)

        newRecordentryNameAdditionalInfo = Entry(
            newRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varAdditionalInfo)
        newRecordentryNameAdditionalInfo.grid(row=5, column=1, sticky=E)

        btnNameNewRecordSave = Button(
            newRecordFrame3, text="SAVE", font=("arial", 20, "bold"), command=self.funcNewRecordDbExecute)
        btnNameNewRecordSave.pack(side=LEFT,
                                  expand=True, pady=10, ipadx=70, ipady=5)

        btnNameNewRecordSave = Button(
            newRecordFrame3, text="CLEAR FIELDS", font=("arial", 20, "bold"), command=self.funcNewRecordClearFields)
        btnNameNewRecordSave.pack(side=LEFT,
                                  expand=True, pady=10, ipadx=70, ipady=5)

        def quit_window():
            self.btnNameNewRecord.config(command=self.funcNewRecord)
            self.newRecordTopLevel.destroy()

        self.newRecordTopLevel.protocol("WM_DELETE_WINDOW", quit_window)

    def funcNewRecordDateRaised(self):
        self.newRecordDateRaisedTopLevel = Toplevel(self.root)
        self.newRecordDateRaisedTopLevel.geometry("400x400+0+0")
        self.newRecordDateRaisedTopLevel.title("SELECT DATE")

        today = datetime.date.today()

        self.DateRaisedCal = Calendar(self.newRecordDateRaisedTopLevel, selectmode='day',
                                      year=today.year, month=today.month,
                                      day=today.day)
        self.DateRaisedCal.pack(padx=20, pady=20, expand=True)

        btnDateRaisedOk = Button(self.newRecordDateRaisedTopLevel, text="SAVE", font=(
            "arial", 20, "bold"), command=self.funcNewRecordDateRaisedFinal)
        btnDateRaisedOk.pack(padx=20, pady=20, expand=True)

    def funcNewRecordDateRaisedFinal(self):

        self.newRecordDateRaisedTopLevel.destroy()

        dt = self.DateRaisedCal.get_date()
        dt1 = datetime.datetime.strptime(dt, '%d/%m/%Y')
        self.varDateRaisedShow = dt1.strftime("%d-%m-%Y")
        self.varDateRaised = dt1.strftime("%Y-%m-%d")

        entryNameDateRaised = Label(self.newRecordFrame1, text=self.varDateRaisedShow, font=(
            "arial", 20, "bold"))
        entryNameDateRaised.grid(row=1, column=1)

    def funcNewRecordDeliveryDate(self):
        self.newRecordDeliveryDateTopLevel = Toplevel(self.root)
        self.newRecordDeliveryDateTopLevel.geometry("400x400+0+0")
        self.newRecordDeliveryDateTopLevel.title("SELECT DATE")

        today = datetime.date.today()

        self.DeliveryDateCal = Calendar(self.newRecordDeliveryDateTopLevel, selectmode='day',
                                        year=today.year, month=today.month,
                                        day=today.day)
        self.DeliveryDateCal.pack(padx=20, pady=20, expand=True)

        btnDeliveryDateOk = Button(self.newRecordDeliveryDateTopLevel, text="SAVE", font=(
            "arial", 20, "bold"), command=self.funcNewRecordDeliveryDateFinal)
        btnDeliveryDateOk.pack(padx=20, pady=20, expand=True)

    def funcNewRecordDeliveryDateFinal(self):

        self.newRecordDeliveryDateTopLevel.destroy()

        dt = self.DeliveryDateCal.get_date()
        dt1 = datetime.datetime.strptime(dt, '%d/%m/%Y')
        self.varDeliveryDateShow = dt1.strftime("%d-%m-%Y")
        self.varDeliveryDate = dt1.strftime("%Y-%m-%d")

        entryNameDeliveryDate = Label(self.newRecordFrame1, text=self.varDeliveryDateShow, font=(
            "arial", 20, "bold"))
        entryNameDeliveryDate.grid(row=5, column=1)

    def funcNewRecordUploadSpecsFileFirst(self):

        self.btnNameUploadSpecs.config(command="")
        self.varNewRecordSelectFileType = StringVar()

        self.newRecordUploadSpecsFileTopLevel = Toplevel(self.root)
        self.newRecordUploadSpecsFileTopLevel.geometry("400x600+0+0")
        self.newRecordUploadSpecsFileTopLevel.title("SELECT FILE TYPE")

        lblNameSelectExtension = Label(
            self.newRecordUploadSpecsFileTopLevel, text="SELECT FILE TYPE", font=("arial", 20, "bold"))
        lblNameSelectExtension.pack(side=TOP, expand=True)

        newRecordcomboboxNameModeOfProc = ttk.Combobox(
            self.newRecordUploadSpecsFileTopLevel, font=("arial", 20, "bold"), textvariable=self.varNewRecordSelectFileType)
        newRecordcomboboxNameModeOfProc.pack(side=TOP, expand=True)

        newRecordcomboboxNameModeOfProc['value'] = (
            "SELECT", ".pdf", ".docx", ".txt")

        btnNameNewRecordUploadExtensionSpecsFile = Button(
            self.newRecordUploadSpecsFileTopLevel, text="SELECT FILE TO UPLOAD", font=("arial", 20, "bold"), command=self.funcNewRecordUploadSpecsFileSecond)
        btnNameNewRecordUploadExtensionSpecsFile.pack(side=TOP, expand=True)

        def quit_window():
            self.btnNameUploadSpecs.config(
                command=self.funcNewRecordUploadSpecsFileFirst)
            self.newRecordUploadSpecsFileTopLevel.destroy()

        self.newRecordUploadSpecsFileTopLevel.protocol(
            "WM_DELETE_WINDOW", quit_window)

    def funcNewRecordUploadSpecsFileSecond(self):
        self.btnNameUploadSpecs.config(
            command=self.funcNewRecordUploadSpecsFileFirst)
        self.newRecordUploadSpecsFileTopLevel.destroy()

        if self.varNewRecordSelectFileType.get() == ".pdf" or self.varNewRecordSelectFileType.get() == ".docx" or self.varNewRecordSelectFileType.get() == ".txt":
            if self.varNewRecordSelectFileType.get() == ".pdf":
                fn = filedialog.askopenfilename(title="Select File", filetypes=[
                    ("Pdf File", "*.pdf")], parent=self.newRecordTopLevel)
            if self.varNewRecordSelectFileType.get() == ".docx":
                fn = filedialog.askopenfilename(title="Select File", filetypes=[
                    ("Word File", "*.docx")], parent=self.newRecordTopLevel)
            if self.varNewRecordSelectFileType.get() == ".txt":
                fn = filedialog.askopenfilename(title="Select File", filetypes=[
                    ("Text File", "*.txt")], parent=self.newRecordTopLevel)

            if fn != "":
                with open(fn, "rb") as f:
                    self.uploadSpecsBinaryData = f.read()

        else:
            messagebox.showinfo("INFO", "SELECT A FILE TYPE",
                                parent=self.newRecordTopLevel)

    def funcNewRecordClearFields(self):

        # self.varModeOfProc = ""

        # self.varDateRaisedShow = ""

        # self.varDeliveryDate = ""

        self.newRecordTopLevel.destroy()
        self.funcNewRecord()

    def funcNewRecordDbExecute(self):

        if self.varActualAmount.get() == "" or self.varAdditionalInfo.get() == "" or self.varAmountEstimate.get() == 0.0 or self.varAmountEstimate.get() == "" or self.varDateRaised == "" or self.varDeliveryDate == "" or self.varDivision.get() == "" or self.varIndentNo.get() == "" or self.varIndentorName.get() == "" or self.varItemDesc.get() == "" or self.varModeOfProc.get() == "" or self.varModeOfProc.get() == "SELECT" or self.uploadSpecsBinaryData == "" or self.varStatus.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.newRecordTopLevel)
        else:
            try:
                # Connect to an existing database
                err1 = False
                conn = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        port="5432",
                                        database="inv_man_sys_db")

                # Create a cursor to perform database operations
                cur = conn.cursor()

                sql = "INSERT INTO purchase_details_tbl (indent_no,date_raised,item_descrp,division,indentor_name,delivery_date,mode_of_procurement,specs,amount_estimate,status,actual_amount,additional_info,extension) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cur.execute(sql, (

                    self.varIndentNo.get(),
                    self.varDateRaised,
                    self.varItemDesc.get(),
                    self.varDivision.get(),
                    self.varIndentorName.get(),
                    self.varDeliveryDate,
                    self.varModeOfProc.get(),
                    (self.uploadSpecsBinaryData, ),
                    self.varAmountEstimate.get(),
                    self.varStatus.get(),
                    self.varActualAmount.get(),
                    self.varAdditionalInfo.get(),
                    self.varNewRecordSelectFileType.get()



                ))

            except (Error) as error:
                err1 = True
                messagebox.showerror(
                    "DATABASE ERROR", error, parent=self.newRecordTopLevel)
                print("Error while connecting to PostgreSQL", error)
            finally:
                if (conn and err1 == False):
                    cur.close()
                    conn.commit()
                    conn.close()
                    print("PostgreSQL connection is closed")
                    messagebox.showinfo(
                        "INFO", "DATA SAVED SUCCESSFULLY", parent=self.newRecordTopLevel)

    def funcUpdateRecord(self):

        self.btnNameUpdateRecord.config(command="")

        self.updateRecordTopLevel = Toplevel(self.root)
        self.updateRecordTopLevel.geometry("1540x950+0+0")
        self.updateRecordTopLevel.title("UPDATE RECORD")

        self.varGetUpdateRecord = StringVar()

        self.varUpdateRecordDateRaised = StringVar()
        self.varUpdateRecordItemDesc = StringVar()
        self.varUpdateRecordDivision = StringVar()
        self.varUpdateRecordIndentorName = StringVar()
        self.varUpdateRecordDeliveryDate = StringVar()
        self.varUpdateRecordModeOfProc = StringVar()
        self.varUpdateRecordAmountEstimate = DoubleVar()
        self.varUpdateRecordStatus = StringVar()
        self.varUpdateRecordActualAmount = DoubleVar()
        self.varUpdateRecordAdditionalInfo = StringVar()

        lbltitle = Label(self.updateRecordTopLevel, bd=20, relief=RIDGE, text="UPDATE RECORD",
                         fg="red", bg="white", font=("times new roman", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        self.UpdateRecordenterIndentNoFrame = Frame(
            self.updateRecordTopLevel, bd=20, relief=RIDGE)
        self.UpdateRecordenterIndentNoFrame.pack(fill=BOTH, expand=True,
                                                 padx=(10, 10), pady=(20, 10))

        updateRecordTreeViewFrame = LabelFrame(
            self.updateRecordTopLevel, bd=20, relief=RIDGE)
        updateRecordTreeViewFrame.pack(
            fill=BOTH, expand=True, padx=(10, 10), pady=(10, 10))

        UpdateRecorddataFrame = LabelFrame(self.updateRecordTopLevel, bd=20, relief=RIDGE, font=(
            "arial", 30, "bold"), text="UPDATE RECORD DETAILS")
        UpdateRecorddataFrame.pack(
            fill=BOTH, expand=True, padx=10, pady=(10, 10))

        self.UpdateRecordnewRecordFrame1 = Frame(
            UpdateRecorddataFrame, bd=20, relief=RIDGE)
        self.UpdateRecordnewRecordFrame1.pack(side=LEFT, fill=BOTH, expand=True,
                                              padx=(10, 5), pady=(10, 10))

        UpdateRecordnewRecordFrame2 = Frame(
            UpdateRecorddataFrame, bd=20, relief=RIDGE)
        UpdateRecordnewRecordFrame2.pack(side=LEFT, fill=BOTH,
                                         expand=True, padx=(5, 10), pady=(10, 10))

        UpdateRecordnewRecordFrame3 = Frame(
            self.updateRecordTopLevel, bd=20, relief=RIDGE)
        UpdateRecordnewRecordFrame3.pack(fill=BOTH,
                                         expand=True, padx=(10, 10), pady=(0, 10))

        self.UpdateRecordlblNameEnterIndent = Label(
            self.UpdateRecordenterIndentNoFrame, text="ENTER INDENT NO", font=("arial", 20, "bold"))
        self.UpdateRecordlblNameEnterIndent.pack(side=LEFT, expand=True)

        self.UpdateRecordentryNameEnterIndent = Entry(
            self.UpdateRecordenterIndentNoFrame, font=("arial", 20, "bold"), textvariable=self.varGetUpdateRecord)
        self.UpdateRecordentryNameEnterIndent.pack(side=LEFT, expand=True)

        self.UpdateRecordbtnSearchEnterIndent = Button(
            self.UpdateRecordenterIndentNoFrame, text="SEARCH", font=("arial", 20, "bold"), command=self.funcGetUpdateRecord)
        self.UpdateRecordbtnSearchEnterIndent.pack(side=LEFT, expand=True)

        self.updateRecordTreeView = ttk.Treeview(updateRecordTreeViewFrame, column=("date_raised", "item_descrp", "division", "indentor_name", "delivery_date",
                                                 "mode_of_procurement", "amount_estimate", "status", "actual_amount", "additional_info"), height=2)

        self.updateRecordTreeView.pack(fill=X, expand=1)

        style = ttk.Style()
        style.configure("Treeview.Heading",
                        font=(None, 10, BOLD))

        scroll_x = ttk.Scrollbar(
            updateRecordTreeViewFrame, orient=HORIZONTAL, command=self.updateRecordTreeView.xview)

        scroll_x.pack(side=BOTTOM, fill=X)

        self.updateRecordTreeView.configure(xscrollcommand=scroll_x.set)

        self.updateRecordTreeView.heading("date_raised", text="DATE RAISED")
        self.updateRecordTreeView.heading(
            "item_descrp", text="ITEM DESCRIPTION")
        self.updateRecordTreeView.heading("division", text="DIVISION")
        self.updateRecordTreeView.heading(
            "indentor_name", text="INDENTOR NAME")
        self.updateRecordTreeView.heading(
            "delivery_date", text="DELIVERY DATE")
        self.updateRecordTreeView.heading(
            "mode_of_procurement", text="MODE OF PROCUREMENT")
        self.updateRecordTreeView.heading(
            "amount_estimate", text="AMOUNT ESTIMATE")
        self.updateRecordTreeView.heading("status", text="STATUS")
        self.updateRecordTreeView.heading(
            "actual_amount", text="ACTUAL AMOUNT")
        self.updateRecordTreeView.heading(
            "additional_info", text="ADDITIONAL INFO")

        self.updateRecordTreeView.column(
            "date_raised", width=140, anchor=CENTER)
        self.updateRecordTreeView.column(
            "item_descrp", width=140, anchor=CENTER)
        self.updateRecordTreeView.column("division", width=140, anchor=CENTER)
        self.updateRecordTreeView.column(
            "indentor_name", width=140, anchor=CENTER)
        self.updateRecordTreeView.column(
            "delivery_date", width=140, anchor=CENTER)
        self.updateRecordTreeView.column(
            "mode_of_procurement", width=170, anchor=CENTER)
        self.updateRecordTreeView.column(
            "amount_estimate", width=140, anchor=CENTER)
        self.updateRecordTreeView.column("status", width=140, anchor=CENTER)
        self.updateRecordTreeView.column(
            "actual_amount", width=140, anchor=CENTER)
        self.updateRecordTreeView.column(
            "additional_info", width=140, anchor=CENTER)

        self.updateRecordTreeView["show"] = "headings"
        self.updateRecordTreeView.bind(
            "<ButtonRelease-1>", self.funcUpdateRecordGetCursor)

        # lblNameIndent = Label(
        #     newRecordFrame1, text="INDENT NO", font=("arial", 20, "bold"))
        # lblNameIndent.grid(row=0, column=0)

        # entryNameIndent = Entry(
        #     newRecordFrame1, font=("arial", 20, "bold"))
        # entryNameIndent.grid(row=0, column=1)

        UpdateRecordlblNameDateRaised = Label(
            self.UpdateRecordnewRecordFrame1, text="DATE RAISED", font=("arial", 20, "bold"))
        UpdateRecordlblNameDateRaised.grid(row=1, column=0, sticky=W)

        self.UpdateRecordbtnNameDateRaised = Button(self.UpdateRecordnewRecordFrame1, text="EDIT", font=(
            "arial", 10, "bold"), command=self.funcSelectUpdateRecordDateRaised)
        self.UpdateRecordbtnNameDateRaised.grid(row=1, column=2, padx=20)

        self.UpdateRecordbtnNameDateRaised["state"] = "disabled"

        UpdateRecordlblNameItemDesc = Label(
            self.UpdateRecordnewRecordFrame1, text="ITEM DESCRP", font=("arial", 20, "bold"))
        UpdateRecordlblNameItemDesc.grid(row=2, column=0, sticky=W)

        UpdateRecordentryNameItemDesc = Entry(
            self.UpdateRecordnewRecordFrame1, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordItemDesc)
        UpdateRecordentryNameItemDesc.grid(row=2, column=1)

        UpdateRecordlblNameDivName = Label(
            self.UpdateRecordnewRecordFrame1, text="DIVISION", font=("arial", 20, "bold"))
        UpdateRecordlblNameDivName.grid(row=3, column=0, sticky=W)

        UpdateRecordentryNameDivName = Entry(
            self.UpdateRecordnewRecordFrame1, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordDivision)
        UpdateRecordentryNameDivName.grid(row=3, column=1)

        UpdateRecordlblNameIndentorName = Label(
            self.UpdateRecordnewRecordFrame1, text="INDENTOR NAME", font=("arial", 20, "bold"))
        UpdateRecordlblNameIndentorName.grid(row=4, column=0, sticky=W)

        UpdateRecordentryNameIndentorName = Entry(
            self.UpdateRecordnewRecordFrame1, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordIndentorName)
        UpdateRecordentryNameIndentorName.grid(row=4, column=1)

        UpdateRecordlblNameDeliveryDate = Label(
            self.UpdateRecordnewRecordFrame1, text="DELIVERY DATE", font=("arial", 20, "bold"))
        UpdateRecordlblNameDeliveryDate.grid(row=5, column=0, sticky=W)

        self.UpdateRecordbtnNameDeliveryDate = Button(self.UpdateRecordnewRecordFrame1, text="EDIT", font=(
            "arial", 10, "bold"), command=self.funcSelectUpdateRecordDeliveryDate)
        self.UpdateRecordbtnNameDeliveryDate.grid(row=5, column=2, padx=20)

        self.UpdateRecordbtnNameDeliveryDate["state"] = "disabled"

        UpdateRecordlblNameModeOfProc = Label(
            UpdateRecordnewRecordFrame2, text="MODE OF PROCUREMENT", font=("arial", 20, "bold"))
        UpdateRecordlblNameModeOfProc.grid(row=0, column=0, sticky=W)

        newRecordcomboboxNameModeOfProc = ttk.Combobox(
            UpdateRecordnewRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordModeOfProc)
        newRecordcomboboxNameModeOfProc.grid(row=0, column=1, sticky=E)

        newRecordcomboboxNameModeOfProc['value'] = (
            "SELECT", "GEM", "OPEN TENDER", "LIMITED TENDER")

        UpdateRecordlblNameSpecs = Label(
            UpdateRecordnewRecordFrame2, text="SPECS", font=("arial", 20, "bold"))
        UpdateRecordlblNameSpecs.grid(row=1, column=0, sticky=W)

        self.UpdateRecordbtnSpecsView = Button(
            UpdateRecordnewRecordFrame2, text="VIEW FILE", font=("arial", 10, "bold"), command=self.funcUpdateRecordSpecsViewFile)
        self.UpdateRecordbtnSpecsView.grid(row=1, column=1, sticky=W)

        self.UpdateRecordbtnSpecsView["state"] = "disabled"

        self.UpdateRecordbtnSpecsEdit = Button(
            UpdateRecordnewRecordFrame2, text="UPLOAD NEW FILE", font=("arial", 10, "bold"), command=self.funcUpdateRecordSpecsUploadNewFileFirst)
        self.UpdateRecordbtnSpecsEdit.grid(row=1, column=1, sticky=E)

        self.UpdateRecordbtnSpecsEdit["state"] = "disabled"

        UpdateRecordlblNameAmountEstimate = Label(
            UpdateRecordnewRecordFrame2, text="AMOUNT ESTIMATE", font=("arial", 20, "bold"))
        UpdateRecordlblNameAmountEstimate.grid(row=2, column=0, sticky=W)

        UpdateRecordentryNameAmountEstimate = Entry(
            UpdateRecordnewRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordAmountEstimate)
        UpdateRecordentryNameAmountEstimate.grid(row=2, column=1)

        UpdateRecordlblNameStatus = Label(
            UpdateRecordnewRecordFrame2, text="STATUS", font=("arial", 20, "bold"))
        UpdateRecordlblNameStatus.grid(row=3, column=0, sticky=W)

        UpdateRecordentryNameStatus = Entry(
            UpdateRecordnewRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordStatus)
        UpdateRecordentryNameStatus.grid(row=3, column=1)

        UpdateRecordlblNameActualAmount = Label(
            UpdateRecordnewRecordFrame2, text="ACTUAL AMOUNT", font=("arial", 20, "bold"))
        UpdateRecordlblNameActualAmount.grid(row=4, column=0, sticky=W)

        UpdateRecordentryNameActualAmount = Entry(
            UpdateRecordnewRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordActualAmount)
        UpdateRecordentryNameActualAmount.grid(row=4, column=1)

        UpdateRecordlblNameAdditionalInfo = Label(
            UpdateRecordnewRecordFrame2, text="ADDITIONAL INFO", font=("arial", 20, "bold"))
        UpdateRecordlblNameAdditionalInfo.grid(row=5, column=0, sticky=W)

        UpdateRecordentryNameAdditionalInfo = Entry(
            UpdateRecordnewRecordFrame2, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordAdditionalInfo)
        UpdateRecordentryNameAdditionalInfo.grid(row=5, column=1)

        self.UpdateRecordbtnNameNewRecordSave = Button(
            UpdateRecordnewRecordFrame3, text="SAVE", font=("arial", 20, "bold"), command=self.funcUpdateRecordDbExecute)
        self.UpdateRecordbtnNameNewRecordSave.pack(side=TOP,
                                                   expand=True, pady=10, ipadx=70, ipady=5)

        self.UpdateRecordbtnNameNewRecordSave["state"] = "disabled"

        def quit_window():
            self.btnNameUpdateRecord.config(command=self.funcUpdateRecord)
            self.updateRecordTopLevel.destroy()

        self.updateRecordTopLevel.protocol("WM_DELETE_WINDOW", quit_window)

    def funcUpdateRecordGetCursor(self, event=""):
        cursor_row = self.updateRecordTreeView.focus()
        content = self.updateRecordTreeView.item(cursor_row)
        row = content["values"]
        self.varUpdateRecordDateRaised = row[0]
        self.varUpdateRecordDeliveryDate = row[4]
        self.varUpdateRecordItemDesc.set(row[1])
        self.varUpdateRecordDivision.set(row[2])
        self.varUpdateRecordIndentorName.set(row[3])
        self.varUpdateRecordModeOfProc.set(row[5])
        self.varUpdateRecordAmountEstimate.set(row[6])
        self.varUpdateRecordStatus.set(row[7])
        self.varUpdateRecordActualAmount.set(row[8])
        self.varUpdateRecordAdditionalInfo.set(row[9])

        dt1 = self.varUpdateRecordDateRaised
        dt2 = datetime.datetime.strptime(dt1, '%Y-%m-%d')
        self.varUpdateRecordDateRaisedShow = dt2.strftime("%d-%m-%Y")

        UpdateRecordentryNameDateRaised = Label(self.UpdateRecordnewRecordFrame1, text=self.varUpdateRecordDateRaisedShow, font=(
            "arial", 20, "bold"))
        UpdateRecordentryNameDateRaised.grid(row=1, column=1)

        dt3 = self.varUpdateRecordDeliveryDate
        dt4 = datetime.datetime.strptime(dt3, '%Y-%m-%d')
        self.varUpdateRecordDeliveryDateShow = dt4.strftime("%d-%m-%Y")

        UpdateRecordentryNameDeliveryDate = Label(self.UpdateRecordnewRecordFrame1, text=self.varUpdateRecordDeliveryDateShow, font=(
            "arial", 20, "bold"))
        UpdateRecordentryNameDeliveryDate.grid(row=5, column=1)

        self.UpdateRecordbtnSpecsView["state"] = "normal"
        self.UpdateRecordbtnSpecsEdit["state"] = "normal"
        self.UpdateRecordbtnNameNewRecordSave["state"] = "normal"
        self.UpdateRecordbtnNameDateRaised["state"] = "normal"
        self.UpdateRecordbtnNameDeliveryDate["state"] = "normal"

    def funcSelectUpdateRecordDateRaised(self):

        self.UpdateRecordDateRaisedTopLevel = Toplevel(self.root)
        self.UpdateRecordDateRaisedTopLevel.geometry("400x400+0+0")
        self.UpdateRecordDateRaisedTopLevel.title("SELECT DATE")

        today = datetime.date.today()

        self.UpdateDateRaisedCal = Calendar(self.UpdateRecordDateRaisedTopLevel, selectmode='day',
                                            year=today.year, month=today.month,
                                            day=today.day)
        self.UpdateDateRaisedCal.pack(padx=20, pady=20, expand=True)

        btnDateRaisedOk = Button(self.UpdateRecordDateRaisedTopLevel, text="SAVE", font=(
            "arial", 20, "bold"), command=self.funcSelectUpdateRecordDateRaisedFinal)
        btnDateRaisedOk.pack(padx=20, pady=20, expand=True)

    def funcSelectUpdateRecordDateRaisedFinal(self):

        self.UpdateRecordDateRaisedTopLevel.destroy()

        dt = self.UpdateDateRaisedCal.get_date()
        dt1 = datetime.datetime.strptime(dt, '%d/%m/%Y')
        self.varUpdateRecordDateRaisedShow = dt1.strftime("%d-%m-%Y")
        self.varUpdateRecordDateRaised = dt1.strftime("%Y-%m-%d")

        UpdateRecordentryNameDateRaised = Label(self.UpdateRecordnewRecordFrame1, text=self.varUpdateRecordDateRaisedShow, font=(
            "arial", 20, "bold"))
        UpdateRecordentryNameDateRaised.grid(row=1, column=1)

    def funcSelectUpdateRecordDeliveryDate(self):

        self.UpdateRecordDeliveryDateTopLevel = Toplevel(self.root)
        self.UpdateRecordDeliveryDateTopLevel.geometry("400x400+0+0")
        self.UpdateRecordDeliveryDateTopLevel.title("SELECT DATE")

        today = datetime.date.today()

        self.UpdateRecordDeliveryDateCal = Calendar(self.UpdateRecordDeliveryDateTopLevel, selectmode='day',
                                                    year=today.year, month=today.month,
                                                    day=today.day)
        self.UpdateRecordDeliveryDateCal.pack(padx=20, pady=20, expand=True)

        btnDeliveryDateOk = Button(self.UpdateRecordDeliveryDateTopLevel, text="SAVE", font=(
            "arial", 20, "bold"), command=self.funcSelectUpdateRecordDeliveryDateFinal)
        btnDeliveryDateOk.pack(padx=20, pady=20, expand=True)

    def funcSelectUpdateRecordDeliveryDateFinal(self):

        self.UpdateRecordDeliveryDateTopLevel.destroy()

        dt = self.UpdateRecordDeliveryDateCal.get_date()
        dt1 = datetime.datetime.strptime(dt, '%d/%m/%Y')
        self.varUpdateRecordDeliveryDateShow = dt1.strftime("%d-%m-%Y")
        self.varUpdateRecordDeliveryDate = dt1.strftime("%Y-%m-%d")

        UpdateRecordentryNameDeliveryDate = Label(self.UpdateRecordnewRecordFrame1, text=self.varUpdateRecordDeliveryDateShow, font=(
            "arial", 20, "bold"))
        UpdateRecordentryNameDeliveryDate.grid(row=5, column=1)

    def funcUpdateRecordSpecsViewFile(self):

        if 1 == 1:
            try:
                err1 = False
                err2 = False
                # Connect to an existing database
                conn = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        port="5432",
                                        database="inv_man_sys_db")

                # Create a cursor to perform database operations
                cur = conn.cursor()

                sql = "SELECT specs , extension FROM purchase_details_tbl WHERE indent_no=%s"

                cur.execute(sql, (self.varGetUpdateRecord.get(),))
                r = cur.fetchall()
                for i in r:
                    data = i[0]
                for i in r:
                    extensionFile = i[1]
                if data != None:
                    if extensionFile == '.pdf':

                        fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), initialfile=f"{self.varGetUpdateRecord.get()}_Specs_File "+str(datetime.datetime.now().strftime("%d-%m-%Y %H%M%S")), title="Save File", defaultextension=".pdf", filetypes=[
                                                          ("Pdf File", "*.pdf")], parent=self.updateRecordTopLevel)
                    if extensionFile == '.docx':

                        fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), initialfile=f"{self.varGetUpdateRecord.get()}_Specs_File "+str(datetime.datetime.now().strftime("%d-%m-%Y %H%M%S")), title="Save File", defaultextension=".docx", filetypes=[
                                                          ("Word File", "*.docx")], parent=self.updateRecordTopLevel)
                    if extensionFile == '.txt':

                        fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), initialfile=f"{self.varGetUpdateRecord.get()}_Specs_File "+str(datetime.datetime.now().strftime("%d-%m-%Y %H%M%S")), title="Save File", defaultextension=".txt", filetypes=[
                                                          ("Text File", "*.txt")], parent=self.updateRecordTopLevel)
                    if fn != "":
                        with open(fn, "wb") as f:
                            f.write(data)
                        f.close()
                if data == None:
                    err2 = True
                    messagebox.showinfo("INFO",
                                        "NO FILE FOUND", parent=self.updateRecordTopLevel)

            except (Error) as error:
                err1 = True
                messagebox.showerror(
                    "DATABASE ERROR", error, parent=self.updateRecordTopLevel)
                print("Error while connecting to PostgreSQL", error)
            finally:
                if (conn and err1 == False and err2 == False and fn != ""):
                    cur.close()
                    conn.commit()
                    conn.close()
                    print("PostgreSQL connection is closed")
                    messagebox.showinfo(
                        "INFO", "FILE DOWNLOADED SUCCESSFULLY", parent=self.updateRecordTopLevel)

    def funcUpdateRecordSpecsUploadNewFileFirst(self):

        self.UpdateRecordbtnSpecsEdit.config(command="")
        self.varUpdateRecordSelectFileType = StringVar()

        self.updateRecordUploadSpecsFileTopLevel = Toplevel(self.root)
        self.updateRecordUploadSpecsFileTopLevel.geometry("400x600+0+0")
        self.updateRecordUploadSpecsFileTopLevel.title("SELECT FILE TYPE")

        lblNameSelectExtension = Label(
            self.updateRecordUploadSpecsFileTopLevel, text="SELECT FILE TYPE", font=("arial", 20, "bold"))
        lblNameSelectExtension.pack(side=TOP, expand=True)

        updateRecordcomboboxNameModeOfProc = ttk.Combobox(
            self.updateRecordUploadSpecsFileTopLevel, font=("arial", 20, "bold"), textvariable=self.varUpdateRecordSelectFileType)
        updateRecordcomboboxNameModeOfProc.pack(side=TOP, expand=True)

        updateRecordcomboboxNameModeOfProc['value'] = (
            "SELECT", ".pdf", ".docx", ".txt")

        btnNameUpdateRecordUploadExtensionSpecsFile = Button(
            self.updateRecordUploadSpecsFileTopLevel, text="SELECT FILE TO UPLOAD", font=("arial", 20, "bold"), command=self.funcUpdateRecordSpecsUploadNewFileSecond)
        btnNameUpdateRecordUploadExtensionSpecsFile.pack(side=TOP, expand=True)

        def quit_window():
            self.UpdateRecordbtnSpecsEdit.config(
                command=self.funcUpdateRecordSpecsUploadNewFileFirst)
            self.updateRecordUploadSpecsFileTopLevel.destroy()

        self.updateRecordUploadSpecsFileTopLevel.protocol(
            "WM_DELETE_WINDOW", quit_window)

    def funcUpdateRecordSpecsUploadNewFileSecond(self):
        self.UpdateRecordbtnSpecsEdit.config(
            command=self.funcUpdateRecordSpecsUploadNewFileFirst)
        self.updateRecordUploadSpecsFileTopLevel.destroy()

        if self.varUpdateRecordSelectFileType.get() == ".pdf" or self.varUpdateRecordSelectFileType.get() == ".docx" or self.varUpdateRecordSelectFileType.get() == ".txt":
            if self.varUpdateRecordSelectFileType.get() == ".pdf":
                fn = filedialog.askopenfilename(title="Select File", filetypes=[
                    ("Pdf File", "*.pdf")], parent=self.updateRecordTopLevel)
            if self.varUpdateRecordSelectFileType.get() == ".docx":
                fn = filedialog.askopenfilename(title="Select File", filetypes=[
                    ("Word File", "*.docx")], parent=self.updateRecordTopLevel)
            if self.varUpdateRecordSelectFileType.get() == ".txt":
                fn = filedialog.askopenfilename(title="Select File", filetypes=[
                    ("Text File", "*.txt")], parent=self.updateRecordTopLevel)

            if fn != "":
                with open(fn, "rb") as f:
                    data = f.read()
                try:
                    err1 = False
                    # Connect to an existing database
                    conn = psycopg2.connect(user="postgres",
                                            password="1234",
                                            host="localhost",
                                            port="5432",
                                            database="inv_man_sys_db")

                    # Create a cursor to perform database operations
                    cur = conn.cursor()

                    sql = "UPDATE purchase_details_tbl SET specs=%s , extension=%s WHERE indent_no=%s"

                    cur.execute(
                        sql, ((data, ), self.varUpdateRecordSelectFileType.get(), self.varGetUpdateRecord.get()))
                    # r = cur.fetchall()
                    # for i in r:
                    #     data = i[0]
                    # with open(fn, "wb") as f:
                    #     f.write(data)
                    # f.close()

                except (Error) as error:
                    err1 = True
                    messagebox.showerror(
                        "DATABASE ERROR", error, parent=self.updateRecordTopLevel)
                    print("Error while connecting to PostgreSQL", error)
                finally:
                    if (conn and err1 == False):
                        cur.close()
                        conn.commit()
                        conn.close()
                        print("PostgreSQL connection is closed")
                        messagebox.showinfo(
                            "INFO", "FILE UPLOADED SUCCESSFULLY", parent=self.updateRecordTopLevel)

        else:
            messagebox.showinfo("INFO", "SELECT A FILE TYPE",
                                parent=self.updateRecordTopLevel)

    def funcGetUpdateRecord(self):
        if self.varGetUpdateRecord.get() == "":
            self.updateRecordTreeView.delete(
                *self.updateRecordTreeView.get_children())
            messagebox.showerror(
                "Error", "Indent No is Required", parent=self.updateRecordTopLevel)

        if self.varGetUpdateRecord.get() != "":
            self.updateRecordTreeView.delete(
                *self.updateRecordTreeView.get_children())
            try:
                # Connect to an existing database
                err1 = False

                conn = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        port="5432",
                                        database="inv_man_sys_db")

                # Create a cursor to perform database operations
                cur = conn.cursor()

                sql = "SELECT indent_no FROM purchase_details_tbl WHERE indent_no=%s"

                cur.execute(sql, (self.varGetUpdateRecord.get(),))
                row1 = cur.fetchall()

            except (Error) as error:
                err1 = True
                messagebox.showerror(
                    "DATABASE ERROR", error, parent=self.updateRecordTopLevel)
                print("Error while connecting to PostgreSQL", error)
            finally:
                if (conn and err1 == False):
                    cur.close()
                    conn.commit()
                    conn.close()
                    print("PostgreSQL connection is closed")
            if len(row1) != 0:

                if row1[0][0] == self.varGetUpdateRecord.get():
                    self.UpdateRecordlblNameEnterIndent.pack_forget()
                    self.UpdateRecordentryNameEnterIndent.pack_forget()
                    self.UpdateRecordbtnSearchEnterIndent.pack_forget()

                    lblNameUpdateRecordIndentNo = Label(
                        self.UpdateRecordenterIndentNoFrame, text="INDENT NO :", font=("arial", 20, "bold"))
                    lblNameUpdateRecordIndentNo.pack(side=LEFT, expand=True)

                    lblNameUpdateRecordIndentNoShow = Label(
                        self.UpdateRecordenterIndentNoFrame, text=self.varGetUpdateRecord.get(), font=("arial", 20, "bold"))
                    lblNameUpdateRecordIndentNoShow.pack(
                        side=LEFT, expand=True)

                    try:
                        # Connect to an existing database
                        err2 = False

                        conn = psycopg2.connect(user="postgres",
                                                password="1234",
                                                host="localhost",
                                                port="5432",
                                                database="inv_man_sys_db")

                        # Create a cursor to perform database operations
                        cur = conn.cursor()

                        sql = "SELECT date_raised,item_descrp,division,indentor_name,delivery_date,mode_of_procurement,amount_estimate,status,actual_amount,additional_info FROM purchase_details_tbl WHERE indent_no=%s"

                        cur.execute(sql, (self.varGetUpdateRecord.get(),))
                        row2 = cur.fetchall()
                        if len(row2) != 0:
                            for i in row2:
                                self.updateRecordTreeView.insert(
                                    "", END, values=i)
                            conn.commit()
                        conn.close()

                    except (Error) as error:
                        err2 = True
                        messagebox.showerror(
                            "DATABASE ERROR", error, parent=self.updateRecordTopLevel)
                        print("Error while connecting to PostgreSQL", error)
                    finally:
                        if (conn and err2 == False):
                            cur.close()
                            print("PostgreSQL connection is closed")
            else:
                messagebox.showinfo(
                    "Info", "indent no. not found", parent=self.updateRecordTopLevel)

    def funcUpdateRecordDbExecute(self):
        if self.varUpdateRecordActualAmount.get() == "" or self.varUpdateRecordAdditionalInfo.get() == "" or self.varUpdateRecordAmountEstimate.get() == 0.0 or self.varUpdateRecordAmountEstimate.get() == "" or self.varUpdateRecordDateRaised == "" or self.varUpdateRecordDeliveryDate == "" or self.varUpdateRecordDivision.get() == "" or self.varGetUpdateRecord.get() == "" or self.varUpdateRecordIndentorName.get() == "" or self.varUpdateRecordItemDesc.get() == "" or self.varUpdateRecordModeOfProc.get() == "" or self.varUpdateRecordModeOfProc.get() == "SELECT" or self.varUpdateRecordStatus.get() == "":
            messagebox.showerror("Error", "Fields Missing",
                                 parent=self.updateRecordTopLevel)
        else:
            try:
                # Connect to an existing database
                err1 = False
                conn = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        port="5432",
                                        database="inv_man_sys_db")

                # Create a cursor to perform database operations
                cur = conn.cursor()

                sql = "UPDATE purchase_details_tbl SET date_raised=%s,item_descrp=%s,division=%s,indentor_name=%s,delivery_date=%s,mode_of_procurement=%s,amount_estimate=%s,status=%s,actual_amount=%s,additional_info=%s WHERE indent_no=%s "

                cur.execute(sql, (



                    self.varUpdateRecordDateRaised,
                    self.varUpdateRecordItemDesc.get(),
                    self.varUpdateRecordDivision.get(),
                    self.varUpdateRecordIndentorName.get(),
                    self.varUpdateRecordDeliveryDate,
                    self.varUpdateRecordModeOfProc.get(),
                    self.varUpdateRecordAmountEstimate.get(),
                    self.varUpdateRecordStatus.get(),
                    self.varUpdateRecordActualAmount.get(),
                    self.varUpdateRecordAdditionalInfo.get(),
                    self.varGetUpdateRecord.get()



                ))

            except (Error) as error:
                err1 = True
                messagebox.showerror(
                    "DATABASE ERROR", error, parent=self.updateRecordTopLevel)
                print("Error while connecting to PostgreSQL", error)
            finally:
                if (conn and err1 == False):
                    cur.close()
                    conn.commit()
                    conn.close()
                    print("PostgreSQL connection is closed")
                    messagebox.showinfo(
                        "INFO", "DATA SAVED SUCCESSFULLY", parent=self.updateRecordTopLevel)

    def funcUploadCSVFile(self):

        fn = filedialog.askopenfilename(
            filetypes=[("Excel file", '.xlsx')])

        if fn != "":

            try:

                err1 = False
                conn_string = 'postgresql://postgres:1234@localhost/inv_man_sys_db'
                db = create_engine(conn_string)
                conn = db.connect()

                df = pd.read_excel(fn)

                df['date_raised'] = df['date_raised'].apply(
                    lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))

                df['delivery_date'] = df['delivery_date'].apply(
                    lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))

                df.to_sql('purchase_details_tbl',
                          con=conn, if_exists='append', index=False)

            except (Error) as error:
                err1 = True
                messagebox.showerror(
                    "DATABASE ERROR", error, parent=root)
                print("Error while connecting to PostgreSQL", error)
            finally:
                if (err1 == False):

                    print("PostgreSQL connection is closed")
                    messagebox.showinfo(
                        "INFO", "DATA INSERTED SUCCESSFULLY", parent=root)


if __name__ == "__main__":
    root = Tk()
    ob = homePage(root)
    root.mainloop()
