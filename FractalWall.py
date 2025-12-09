import threading
import re
import os
import marshal
import string
import base64
import zlib
import ast
import codecs
import pickle
import shutil
from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from random import choices, randint, choice, shuffle

window = Tk()
window.title("FractalWall Obfuscator")
window.geometry("859x709")
window.maxsize(859, 709)
window.minsize(859, 709)
window.iconbitmap("assets/mylogo.ico")
backg = PhotoImage(file='assets/background.png')
browsebu = PhotoImage(file='assets/browse.png')
obfuscatebu = PhotoImage(file='assets/obfuscate.png')

class Fractal:

    def __init__(self):
        self.pathfile = ""
        threading.Thread(target=self._gui).start()

    def _obfuscatestart_(self):
        threading.Thread(target=self._obfuscatestart).start()

    def _obfuscatestart(self):
        if len(self.pathfile) > 1:
            if self.pathfile.endswith(".py"):
                if os.path.exists(self.pathfile):
                    self.filename = os.path.splitext(os.path.basename(self.pathfile))[0]
                    self.newfolder1 = f"{self.filename}-Obfuscated"
                    if os.path.exists(self.newfolder1):
                        shutil.rmtree(self.newfolder1)
                    else:
                        os.mkdir(self.newfolder1)
                    filecont = open(self.pathfile,"r+").read()
                    open(f"{self.newfolder1}/{self.filename}.py","w+").write(filecont)
                    self.file = f"{self.newfolder1}/{self.filename}.py"
                    self.skibidichr = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
                    self.importedmodules = ["zlib","base64","os","sys","marshal","platform","ctypes","subprocess"]
                    self._getimports()
                    self._firstwall()
                    self._secondwall()
                    self._thirdwall()
                    self._thirdwallfinalization()
                    self._fourthwall()
                    threading.Thread(target=self._showsoutputfile).start()
                    messagebox.showinfo("FractalWall Obfuscator",f"Successfully Obfuscated File ! -> {self.newfolder1}/{self.filename}.py")
                else:
                    messagebox.showerror("FractalWall Obfuscator","Cannot find python file")
            else:
                messagebox.showerror("FractalWall Obfuscator","Please select a python file .py")
        else:
            messagebox.showerror("FractalWall Obfuscator","No python file selected silly !")

    def _getimports(self):
        code = open(self.file,'r').read()
        tree = ast.parse(code)
        imports = [node for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom))]
        for import_node in imports:
            if isinstance(import_node, ast.Import):
                for alias in import_node.names:
                    self.importedmodules.append(alias.name)
            elif isinstance(import_node, ast.ImportFrom):
                if import_node.module == 'random':
                    self.importedmodules.append(f"{import_node.module}|{','.join([name.name for name in import_node.names])}")

    def _firstwall(self):
        code = open(self.file, 'r').read()
        forcodemar = ''.join(choices(string.ascii_uppercase + string.digits, k=randint(10,20)))
        code = base64.b16encode(zlib.compress(marshal.dumps(compile(code.encode(),f"{forcodemar}","exec")))).decode()
        code = code.replace('0','/').replace('1',')').replace('2','(').replace('3','*').replace('4','&').replace('5','?').replace('6','%').replace('7','$').replace('8','#').replace('9','@').replace('A','!').replace('B',',').replace('C','.').replace('D',':').replace('E',';').replace('F','^')
        part1 = code[:len(code) // 2]
        part2 = code[len(code) // 2:]
        os.mkdir(f"{self.newfolder1}/cache")
        open(f"{self.newfolder1}/cache/os.py","w+").write(f"def root_windows():\n\treturn '{part1}'")
        open(f"{self.newfolder1}/cache/sys.py","w+").write(f"def root_system():\n\treturn '{part2}'")
        self._createfirstwall()
    def _createfirstwall(self):
        code = """import zlib,base64,os,sys,marshal
from cache.os import root_windows
from cache.sys import root_system
part1 = root_windows()
part2 = root_system()
combined_code = part1 + part2
combined_code = combined_code.replace('^', 'F').replace(';', 'E').replace(':', 'D').replace('.', 'C').replace(',', 'B').replace('!', 'A').replace('@', '9').replace('#', '8').replace('$', '7').replace('%', '6').replace('?', '5').replace('&', '4').replace('*', '3').replace('(', '2').replace(')', '1').replace('/', '0')
exec(marshal.loads(zlib.decompress(base64.b16decode(combined_code.encode()))))
"""
        forcodemar = ''.join(choices(string.ascii_uppercase + string.digits, k=randint(10,20)))
        code = base64.b64encode(marshal.dumps(compile(code.encode(),f"{forcodemar}","exec"))).decode()
        open(f"{self.newfolder1}/{self.filename}.py","w+").write(fr"import marshal,base64;exec(marshal.loads(base64.b64decode('{code}')))")
    
    def _secondwall(self):
        os.system(f"pyarmor gen --output {self.newfolder1} {self.newfolder1}/{self.filename}.py")
        os.system('cls')
    
    def genrandomtutf(self):
        s = ''.join(choices(string.ascii_uppercase + string.digits, k=randint(30,50)))
        s=base64.b16encode(s.encode()).decode()
        s= s.replace('0','°').replace('1','`').replace('2','~').replace('3','¤').replace('4','.').replace('5','¬').replace('6','+').replace('7',',').replace('8','*').replace('9',':').replace('A',';').replace('B','@').replace('C','&').replace('D','=').replace('E','-').replace('F','_')
        return s.encode('utf-16')

    def tochr(self,s):
        newstring = ""
        for i in s:
            newstring += "{"+self.skibidichr+"("+str(bin(ord(i)))+")}"
        return newstring

    def genrandomeval(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=exec"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandomcompile(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=compile"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandombase64(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=__import__('base64').b16decode"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandommarshal(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=__import__('marshal').loads"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandompickle(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=__import__('pickle').loads"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandomzlib(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=__import__('zlib').decompress"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandomcodecs(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=__import__('codecs').decode"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandomchr(self):
        s1=''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        s=f"{s1}=chr"
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        s=base64.b64encode(zlib.compress(marshal.dumps(compile(s.encode(),f"{forcodemar}","exec")))).decode()
        s=self.tochr(s)
        s=f"exec(marshal.loads(zlib.decompress(base64.b64decode(f'{s}'))))"
        return s,s1

    def genrandomname(self):
        return ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(100,120)))

    def newnull(self):
        null = ""
        for _ in range(randint(200,400)):
            null+="\v"
        return null

    def _thirdwall(self):
        self.whichwall = 0
        FILE = open(f"{self.newfolder1}/{self.filename}.py","r+").read()
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        code = codecs.encode(base64.b16encode(zlib.compress(pickle.dumps(marshal.dumps(compile(FILE.encode(),f"{forcodemar}","exec"))))).decode(),"rot13")
        code = code.replace('0','°').replace('1','`').replace('2','~').replace('3','¤').replace('4','.').replace('5','¬').replace('6','+').replace('7',',').replace('8','*').replace('9',':').replace('A',';').replace('B','@').replace('C','&').replace('D','=').replace('E','-').replace('F','_')
        code = code.encode("utf-16")
        self.exec1, self.exec2 = self.genrandomeval()
        replace2 = "replace"
        self.b641, self.b642 = self.genrandombase64()
        self.mar1, self.mar2 = self.genrandommarshal()
        self.pickl1, self.pickl2 = self.genrandompickle()
        self.zlib1, self.zlib2 = self.genrandomzlib()
        self.codec1, self.codec2 = self.genrandomcodecs()
        self.chr1, self.chr2 = self.genrandomchr()
        self.listofrepl = [f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b10110000)}',f'"+"{"+f"{self.chr2}"+"(0b110000)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b1100000)}',f'"+"{"+f"{self.chr2}"+"(0b110001)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b1111110)}',f'"+"{"+f"{self.chr2}"+"(0b110010)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b10100100)}',f'"+"{"+f"{self.chr2}"+"(0b110011)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b101110)}',f'"+"{"+f"{self.chr2}"+"(0b110100)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b10101100)}',f'"+"{"+f"{self.chr2}"+"(0b110101)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b101011)}',f'"+"{"+f"{self.chr2}"+"(0b110110)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b101100)}',f'"+"{"+f"{self.chr2}"+"(0b110111)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b101010)}',f'"+"{"+f"{self.chr2}"+"(0b111000)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b111010)}',f'"+"{"+f"{self.chr2}"+"(0b111001)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b111011)}',f'"+"{"+f"{self.chr2}"+"(0b1000001)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b1000000)}',f'"+"{"+f"{self.chr2}"+"(0b1000010)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b100110)}',f'"+"{"+f"{self.chr2}"+"(0b1000011)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b111101)}',f'"+"{"+f"{self.chr2}"+"(0b1000100)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b101101)}',f'"+"{"+f"{self.chr2}"+"(0b1000101)}')",f".{replace2}(f'"+"{"+f"{self.chr2}"+"(0b1011111)}',f'"+"{"+f"{self.chr2}"+"(0b1000110)}')"]
        old_name = self.genrandomname()
        CODE=""
        CODE+=f"{old_name}={code}.decode('utf-16')\n"
        used_list = []
        while len(used_list) != 16:
            new_name = self.genrandomname()
            cblue = randint(0,15)
            if cblue not in used_list:
                CODE+=f"{new_name}={old_name}{self.listofrepl[cblue]}\n"
                old_name = new_name
                used_list.append(cblue)
        new_name = self.genrandomname()
        CODE+=f"{new_name}={self.codec2}({old_name}"+",f'{"+self.chr2+"(0b1110010)}{"+self.chr2+"(0b1101111)}{"+self.chr2+"(0b1110100)}{"+self.chr2+"(0b110001)}{"+self.chr2+"(0b110011)}')"
        old_name = new_name;new_name = self.genrandomname()
        CODE+=f"\n{new_name}={self.b642}({old_name})"
        old_name = new_name;new_name = self.genrandomname()
        CODE+=f"\n{new_name}={self.zlib2}({old_name})"
        old_name = new_name;new_name = self.genrandomname()
        CODE+=f"\n{new_name}={self.pickl2}({old_name})"
        old_name = new_name;new_name = self.genrandomname()
        CODE+=f"\n{new_name}={self.exec2}({self.mar2}({old_name}))"
        open(f"{self.newfolder1}/{self.filename}.py","w+").write(CODE)
    
    def _thirdwallfinalization(self):
        newfile = ""
        FILE = open(f"{self.newfolder1}/{self.filename}.py","r+").readlines()
        for line in FILE:
            newfile += f"{line}#{self.newnull()}\n#{self.newnull()}\n{self.genrandomname()}={self.genrandomtutf()}#{self.newnull()}\n#{self.newnull()}\n"
        open(f"{self.newfolder1}/{self.filename}.py","w+").write(newfile)
    
    def _fourthwall(self):
        TOFUCKUP = []
        FILE = open(f"{self.newfolder1}/{self.filename}.py","r+").read()
        forcodemar = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(20,40)))
        plifpluf = ''.join(choices(string.ascii_uppercase + string.ascii_letters, k=randint(30,50)))
        code = base64.b16encode(zlib.compress(pickle.dumps(marshal.dumps(compile(FILE.encode(),f"{forcodemar}","exec"))))).decode()
        code = code.replace('0','°').replace('1','`').replace('2','~').replace('3','¤').replace('4','.').replace('5','¬').replace('6','+').replace('7',',').replace('8','*').replace('9',':').replace('A',';').replace('B','@').replace('C','&').replace('D','=').replace('E','-').replace('F','_')
        code = code.encode("utf-16")
        BLAWWW = f"""{self.exec1};{self.b641};{self.mar1};{self.pickl1};{self.zlib1};{self.codec1};{self.chr1}""".replace("exec",plifpluf)
        CODE = f"import marshal,base64,zlib,pickle,codecs"
        for mp_ in self.importedmodules:
            if "|" not in mp_:
                if mp_ not in CODE:
                    CODE+=f",{mp_}"
        for mp2_ in self.importedmodules:
            if "|" in mp2_:
                mp2_ = f";from {mp2_.split('|')[0]} import {mp2_.split('|')[1]}"
                if mp2_ not in CODE:
                    CODE+=mp2_
        CODE+=f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t;{self.skibidichr}=getattr(__builtins__,chr(0b1100011)+chr(0b1101000)+chr(0b1110010));{plifpluf}=getattr(__builtins__,{self.skibidichr}(0b1100101)+{self.skibidichr}(0b1111000)+{self.skibidichr}(0b1100101)+{self.skibidichr}(0b1100011));{plifpluf}({BLAWWW.encode('utf-16')}.decode('utf-16'))"
        old_name = self.genrandomname()
        CODE +=f"\n{old_name}={code}.decode('utf-16')"
        firstforreplacement = choice(self.listofrepl)
        used_list = []
        used_list.append(firstforreplacement)
        new_classname = self.genrandomname()
        new_functionname = self.genrandomname()
        TOFUCKUP.append(f"{new_classname}|{new_functionname}")
        CODE+=f"\nclass {new_classname}:\n\tdef {new_functionname}(self):\n\t\treturn {old_name}{firstforreplacement}"
        old_classname = new_classname
        old_functionname = new_functionname
        while len(used_list) != 16:
            new_classname = self.genrandomname()
            new_functionname = self.genrandomname()
            cblue = randint(0,15)
            if self.listofrepl[cblue] not in used_list:
                CODE+=f"\nclass {new_classname}({old_classname}):\n\tdef {new_functionname}(self):\n\t\treturn super().{old_functionname}(){self.listofrepl[cblue]}"
                TOFUCKUP.append(f"{new_classname}|{new_functionname}")
                old_classname = new_classname
                old_functionname = new_functionname
                used_list.append(self.listofrepl[cblue])
        new_classname = self.genrandomname();new_functionname = self.genrandomname()
        CODE+=f"\nclass {new_classname}({old_classname}):\n\tdef {new_functionname}(self):\n\t\treturn {self.b642}(super().{old_functionname}())"
        TOFUCKUP.append(f"{new_classname}|{new_functionname}")
        old_classname = new_classname;old_functionname = new_functionname;new_classname = self.genrandomname();new_functionname = self.genrandomname()
        CODE+=f"\nclass {new_classname}({old_classname}):\n\tdef {new_functionname}(self):\n\t\treturn {self.zlib2}(super().{old_functionname}())"
        TOFUCKUP.append(f"{new_classname}|{new_functionname}")
        old_classname = new_classname;old_functionname = new_functionname;new_classname = self.genrandomname();new_functionname = self.genrandomname()
        CODE+=f"\nclass {new_classname}({old_classname}):\n\tdef {new_functionname}(self):\n\t\treturn {self.pickl2}(super().{old_functionname}())"
        TOFUCKUP.append(f"{new_classname}|{new_functionname}")
        old_classname = new_classname;old_functionname = new_functionname;new_classname = self.genrandomname();new_functionname = self.genrandomname()
        CODE+=f"\nclass {new_classname}({old_classname}):\n\tdef {new_functionname}(self):\n\t\treturn {self.exec2}({self.mar2}(super().{old_functionname}()))\n"
        TOFUCKUP.append(f"{new_classname}|{new_functionname}")
        shuffle(TOFUCKUP)
        for brrr in TOFUCKUP:
            br = str(brrr).split("|")[0]
            brr = str(brrr).split("|")[1]
            CODE += f"{br}().{brr}()\n"
        FILE = open(f"{self.newfolder1}/{self.filename}.py","w+").write(CODE)

    def _browsepy(self):
        path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if path:
            self.Filepathentry.delete(0, "end")
            self.Filepathentry.insert(0, path)
            self.pathfile = ""

    def _outputenlgiht(self,event=None):
        for tag in self.Ouputtext.tag_names():
            self.Ouputtext.tag_remove(tag, "1.0", "end")
        keywords = {"def": "blue","class": "purple","import": "orange","from": "orange","return": "green","if": "red","else": "red","elif": "red","for": "red","while": "red","in": "red","True": "darkgreen","False": "darkgreen","print":"yellow","input":"yellow","super":"purple"}
        content = self.Ouputtext.get("1.0", "end")
        for kw, color in keywords.items():
            for kw, color in keywords.items():
                for match in re.finditer(rf'\b{re.escape(kw)}\b', content, re.MULTILINE):
                    start_index = f"1.0+{match.start()}c"
                    end_index = f"1.0+{match.end()}c"
                    self.Ouputtext.tag_add(kw, start_index, end_index)
                    self.Ouputtext.tag_config(kw, foreground=color)

    def _showsoutputfile(self):
        filepath = os.path.join(self.newfolder1, f"{self.filename}.py")
        self.Ouputtext.delete("1.0", "end")
        foroutput = ""
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.rstrip("\n")
                if len(line) > 1000:
                    line = line[:1000] + "..."
                foroutput += f"{line}\n"
        self.Ouputtext.insert("end", foroutput)
        self._outputenlgiht()

    def _detectnewfile(self):
        while True:
            path = self.Filepathentry.get()
            if len(path) > 1:
                if path.endswith(".py"):
                    if path != self.pathfile:
                        if os.path.exists(path):
                            self.pathfile = path
                            new_content = open(path,"r+").read()
                            self.Inputtext.delete("1.0", "end")
                            self.Inputtext.insert("1.0", new_content)
                            self.Ouputtext.delete("1.0", "end")
                            self._inputenlight()
            sleep(1)

    def _inputenlight(self,event=None):
        for tag in self.Inputtext.tag_names():
            self.Inputtext.tag_remove(tag, "1.0", "end")
        keywords = {"def": "blue","class": "purple","import": "orange","from": "orange","return": "green","if": "red","else": "red","elif": "red","for": "red","while": "red","in": "red","True": "darkgreen","False": "darkgreen","print":"yellow","input":"yellow","super":"purple"}
        content = self.Inputtext.get("1.0", "end")
        for kw, color in keywords.items():
            for kw, color in keywords.items():
                for match in re.finditer(rf'\b{re.escape(kw)}\b', content, re.MULTILINE):
                    start_index = f"1.0+{match.start()}c"
                    end_index = f"1.0+{match.end()}c"
                    self.Inputtext.tag_add(kw, start_index, end_index)
                    self.Inputtext.tag_config(kw, foreground=color)

    def _gui(self):
        Bg = Label(window, image=backg,borderwidth=0)
        Bg.place(x=0, y=0)
        self.Filepathentry = Entry(window,font=('SeoulHangang',10),bg='#D3D3D3', fg='#1A1A1A',width=97,borderwidth=0)
        self.Filepathentry.place(x=54,y=186)
        Browse = Button(window, image=browsebu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._browsepy)
        Browse.place(x=745,y=185)
        Obfuscate = Button(window, image=obfuscatebu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._obfuscatestart_)
        Obfuscate.place(x=354,y=638)
        self.Inputtext = Text(window, bg="#0B0B0B", fg="#FFFFFF",wrap="none",width=44, height=20, borderwidth=0)
        self.Inputtext.place(x=42,y=287)
        self.Ouputtext = Text(window, bg="#0B0B0B", fg="#FFFFFF",wrap="none",width=44, height=20, borderwidth=0)
        self.Ouputtext.place(x=461,y=287)
        threading.Thread(target=self._detectnewfile).start()

Fractal()
window.mainloop()