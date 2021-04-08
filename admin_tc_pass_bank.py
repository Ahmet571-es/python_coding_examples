class National_Number():
    def __init__(self):
        print("Tc kimlik numarasınızı sisteme kaydetmeden admin ve şifre alamassınız...")
        tc=input("Tc kimlik numaranızı giriniz = ")
        tc_list=[]
        tc_okey=True
        self.tc_okey=tc_okey
        for i in range(0,1):
            if len(tc)!=11:
                print("Karakter sayısı 11 olmalıdır.")
                self.tc_okey=False
                break
            elif len(tc)==11:
                if not tc.isdigit():
                    print("Karakterler rakam olmalıdır...")
                    self.tc_okey=False
                    break
                elif tc.isdigit():
                    if int(tc[0])==0:
                        print("İlk rakam 0 olamaz...")
                        self.tc_okey=False
                        break
                    elif int(tc[0])!=0:
                        for i in tc:
                            tc_list.append(int(i))
                        if sum(tc_list[0:10])%10!=tc_list[10]:
                            print("Tc Numaranızda dizim hatası var...")
                            self.tc_okey=False
                            break
                        elif sum(tc_list[0:10])%10==tc_list[10]:
                            a= 7*(sum(tc_list[0:9:2]))
                            b= sum(tc_list[1:8:2])
                            c = (a-b)%10
                            if c!=tc_list[9]:
                                print("Tc numaranızda hata var. Rakam dizinleri yanlış ")
                                self.tc_okey=False
                                break
                            elif c==tc_list[9]:
                                print("Tc numaranızı doğru girdiniz...")                        


class Admin(National_Number):
    def __init__(self):
        National_Number.__init__(self)
        admin_okey=True
        self.admin_okey=admin_okey
        for i in range(0,1):
            if self.tc_okey==False:
                print("Admin giremessiniz, Tc numaranızı sistem onaylamıyor...")
                self.admin_okey=False
                break
            elif self.tc_okey==True:
                print("Kullanıcı adı en az 3 ve en çok 15 karakter olmalıdır. ")
                admin=input("Admin kullanıcı adınızı giriniz .. ")
                if len(admin)<3 or len(admin)>15:
                    print("Karakter sayısı yanlış girildi...")
                    self.admin_okey=False
                    break
                elif len(admin)>=3 or len(admin)<=15:
                    if admin.isdigit():
                        print("Rakam girilemez")
                        self.admin_okey=False
                        break
                    elif not admin.isdigit():    
                        if admin[0]!=admin[0].upper():
                            print("İlk harf büyük olmalıdır...")
                            self.admin_okey=False
                            break
                        elif admin[0]==admin[0].upper():
                            if admin[1:len(admin)]!=admin[1:len(admin)].lower():
                                print("Diğer karakterler küçük olmalıdır..")
                                self.admin_okey=False
                                break
                            elif admin[1:len(admin)]==admin[1:len(admin)].lower():
                                if len(admin)==3:
                                    if admin[1]==admin[2] or admin[1]!=admin[1].replace(" ","") or admin[2]!= admin[2].replace(" ",""):
                                        print("Girilen harfler aynı olamaz ve boşluk bırakılamaz...")
                                        self.admin_okey=False
                                        break
                                    elif admin[1]!=admin[2] and admin[1]==admin[1].replace(" ","") or admin[2]== admin[2].replace(" ",""):
                                        print("Admin girişiniz onaylandı tebrikler...")
                                        print(f"{admin} adlı kullanıcı adınız ile sitemize girebilirsiniz...")
                                elif len(admin)>3 and len(admin)<=15:
                                    if admin[1]==admin[2]==admin[3] or admin[4]==admin[5:len(admin)] or admin[1:len(admin)]!=admin[1:len(admin)].replace(' ',""):
                                        print("Girilen harflerin hepsi aynı olamaz ve boşluk bırakılamaz...")
                                        self.admin_okey=False
                                        break
                                    elif admin[1]!=admin[2]!=admin[3] and admin[4]!=admin[5:len(admin)] and admin[1:len(admin)]==admin[1:len(admin)].replace(' ',""):
                                        print("Admin girişiniz onaylandı tebrikler...")
                                        print(f"{admin} adlı kullanıcı adınız ile sitemize girebilirsiniz...")


class Password(Admin):
    def __init__(self):
        Admin.__init__(self)
        pass_okey=True
        self.pass_okey=pass_okey
        for i in range(0,1):
            if self.tc_okey==False or self.admin_okey==False:
                print("Maalesef giriş yapamassınız")
                break
            elif self.tc_okey==True and self.admin_okey==True:
                sentence=input("Lütfen şifre giriniz = ")
                if len(sentence)!=8:
                    print("Şifreniz 8 karakter değil..")
                    self.pass_okey=False
                    break
                elif len(sentence)==8:
                    a=sentence[0]
                    b=sentence[1]
                    if a.isdigit() or b.isdigit():
                        print("ilk iki harf rakam girilemez...")
                        self.pass_okey=False
                        break
                    elif not a.isdigit() and not b.isdigit():
                        if not a==a.upper():
                            print("ilk harf büyük olmalıdır...")
                            self.pass_okey=False
                            break
                        elif a==a.upper():
                            if not b==b.lower():
                                print("ikinci harf küçük olmalıdır...")
                                self.pass_okey=False
                                break
                            elif b==b.lower():
                                if not sentence[2:8].isdigit():
                                    print("son altı karakter rakam olmalıdır.")
                                    self.pass_okey=False
                                    break
                                elif sentence[2:8].isdigit(): 
                                    if sentence[2]==sentence[3]==sentence[4]==sentence[5]==sentence[6]==sentence[7]:
                                        print("Tüm rakamlar eşit olamaz...")
                                        self.pass_okey=False
                                        break
                                    elif sentence[2]==sentence[3]==sentence[4]==sentence[5]:    
                                        print("son 4 rakam eşit olamaz")
                                        self.pass_okey=False
                                        break     
                                    elif sentence[3]==sentence[4]==sentence[5]:
                                        print("son 3 rakam eşit olamaz")
                                        self.pass_okey=False
                                        break
                                    else:    
                                        print("Şifre işleminiz başarılı bir şekilde onaylandı...")


class Banka_Hesap(Password):
    def __init__(self):
        Password.__init__(self)
        for i in range(0,1):
            if self.tc_okey==False or self.admin_okey==False or self.pass_okey==False:
                print("Maalesef bankamızda Hesap açtıramassınız...")
                break
            elif self.tc_okey==True and self.admin_okey==True and self.pass_okey==True:
                name=input("Lütfen adınızı giriniz. ")
                self.name=name
                surname=input("Lütfen soyadınızı giriniz. ")
                self.surname=surname
                money=int(input("Lütfen yatıracağınız para miktarını giriniz. "))
                self.money=money
                print("İşlemler onaylandı...")
                print(f"{self.name} adı {self.surname} ve soyadı ile toplam tutarı= {self.money} TL olan hesabınız aktiftir.")
