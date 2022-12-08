#include<iostream>
#include<fstream>
#include<conio.h>
#include<string.h>
#include<string>
using namespace std;

char UserInfo[100] = "Information.txt";
int batangas = 0;

struct table {
    char us_firstname[20], us_lastname[20], us_MobileNo[20], us_barangay[20], us_city[20], us_temp[20], us_symptoms[20];
};

class Information {
public:
    void us_pack(table r);
    table us_unpack(char a[]);
    void us_add_data();
    void us_view();
    void ad_search();
    void ad_edit();
};


// USER PANEL
void Information::us_pack(table r) {
    fstream fp;
    fp.open(UserInfo, ios::out | ios::app);
    if (!fp) {
        cout << "\nFile Not Found\n";
        exit(0);
    }
    char buff[100];
    strcpy_s(buff, r.us_firstname);
    strcat_s(buff, "|");
    strcat_s(buff, r.us_lastname);
    strcat_s(buff, "|");
    strcat_s(buff, r.us_MobileNo);
    strcat_s(buff, "|");
    strcat_s(buff, r.us_barangay);
    strcat_s(buff, "|");
    strcat_s(buff, r.us_city);
    strcat_s(buff, "|");
    strcat_s(buff, r.us_temp);
    strcat_s(buff, "|");
    strcat_s(buff, r.us_symptoms);
    strcat_s(buff, "|");
    for (int i = 0; i < 100 - strlen(buff); i++)
        strcat_s(buff, "|");
    fp << buff << endl;
    fp.close();
}


table Information::us_unpack(char buff[]) {
    table r;
    int i = 0, j = 0;
    while (buff[j] != '|')
        r.us_firstname[i++] = buff[j++];
    r.us_firstname[i] = '\0';
    i = 0;
    j++;
    while (buff[j] != '|')
        r.us_lastname[i++] = buff[j++];
    r.us_lastname[i] = '\0';
    i = 0;
    j++;
    while (buff[j] != '|')
        r.us_MobileNo[i++] = buff[j++];
    r.us_MobileNo[i] = '\0';
    i = 0;
    j++;
    while (buff[j] != '|')
        r.us_barangay[i++] = buff[j++];
    r.us_barangay[i] = '\0';
    i = 0;
    j++;
    while (buff[j] != '|')
        r.us_city[i++] = buff[j++];
    r.us_city[i] = '\0';
    i = 0;
    j++;
    while (buff[j] != '|')
        r.us_temp[i++] = buff[j++];
    r.us_temp[i] = '\0';
    i = 0;
    j++;
    while (buff[j] != '|')
        r.us_symptoms[i++] = buff[j++];
    r.us_symptoms[i] = '\0';
    i = 0;
    j++;
    return(r);
}


void Information::us_add_data() {
    table s;
    cout << "\nENTER YOUR FIRST NAME: ";
    cin.ignore();
    cin.getline(s.us_firstname, 20);
    cout << "ENTER YOUR LAST NAME: ";
    cin.getline(s.us_lastname, 20);
    cout << "ENTER YOUR MOBILE NO.: ";
    cin >> s.us_MobileNo;
    cout << "ENTER YOUR BARANGAY: ";
    cin >> s.us_barangay;
    cout << "ENTER YOUR CITY/MUNICIPALITY: ";
    cin.ignore();
    cin.getline(s.us_city, 20);
    cout << "ENTER YOUR TEMPERATURE: ";
    cin.getline(s.us_temp, 20);
    cout << "EXPERIENCING ANY SYMPTOMS? (Type Yes/No): ";
    cin >> s.us_symptoms;

    batangas++;
    us_pack(s);
}


void Information::us_view() {
    fstream fp;
    char buff[100];
    table r;

    fp.open(UserInfo, ios::binary | ios::in);
    if (!fp) {
        cout << "\n\tNo Records Yet!\n";
        return;
    }
    cout << "\nRecords: Batangas Province- " << batangas << endl;
    cout << "========================================================================================================================================================================================================\n";
    cout << "Info No.\tFIRSTNAME\t\tLAST NAME\t\tMOBILE NO.\t\tBARANGAY\t\tCITY/MUNICIPALITY\t\tTEMPERATURE\t\tEXPERIENCING ANY SYMPTOMS?\n";
    cout << "========================================================================================================================================================================================================\n";
    int c = 1;
    while (1) {
        fp.getline(buff, 100);
        if (fp.eof())
            break;
        r = us_unpack(buff);
        cout << c++ << "\t\t" << r.us_firstname << "\t\t\t" << r.us_lastname << "\t\t";
        cout << r.us_MobileNo << "\t\t" << r.us_barangay << "\t\t" << r.us_city << "\t\t\t" << r.us_temp << "\t\t\t\t" << r.us_symptoms << endl;
    }
    fp.close();
    return;
}


// ADMIN PANEL
void Information::ad_search() {
    fstream fp;
    char us_MobileNo[20], buff[100];
    int i, j;
    table s;
    fp.open(UserInfo, ios::in);
    if (!fp) {
        cout << "\n\tNo Records Yet!\n";
        return;
    }
    cout << "\nENTER THE MOBILE NO. TO BE SEARCHED : ";
    cin >> us_MobileNo;
    i = 0;
    while (1) {
        fp.getline(buff, 100);
        if (fp.eof())break;
        s = us_unpack(buff);
        if (strcmp(s.us_MobileNo, us_MobileNo) == 0) {
            cout << "\n INFORMATION FOUND\n";
            cout << "\nFIRST NAME: " << s.us_firstname;
            cout << "\nLAST NAME: " << s.us_lastname;
            cout << "\nMOBILE NO.: " << s.us_MobileNo;
            cout << "\nBARANGAY: " << s.us_barangay;
            cout << "\nCITY/MUNICIPALITY: " << s.us_city;
            cout << "\nTEMPERATURE: " << s.us_temp;
            cout << "\nEXPERIENCING ANY SYMPTOMS?: " << s.us_symptoms;
            cout << endl;
            return;
        }
    }
    cout << "\nInformation NOT FOUND\n";
    return;
}


void Information::ad_edit() {
    fstream fp;
    char us_MobileNo[20], buff[100];
    int i, j, ch;
    table s[100];
    fp.open(UserInfo, ios::in);
    if (!fp) {
        cout << "\n\tNo Records Yet!\n";
        return;
    }
    cout << "\nENTER THE MOBILE NO. OF THE USER : ";
    cin >> us_MobileNo;
    i = 0;
    while (1) {
        fp.getline(buff, 100);
        if (fp.eof())break;
        s[i] = us_unpack(buff);
        i++;
    }
    for (j = 0; j < i; j++) {
        if (strcmp(s[j].us_MobileNo, us_MobileNo) == 0) {
            cout << "USER INFORMATION\n";
            cout << "\nFirst Name: " << s[j].us_firstname;
            cout << "\nLast Name: " << s[j].us_lastname;
            cout << "\nMobile No.: " << s[j].us_MobileNo;
            cout << "\nBarangay: " << s[j].us_barangay;
            cout << "\nCity/Municipality: " << s[j].us_city;
            cout << "\nTemperature: " << s[j].us_temp;
            cout << "\nHave EXPERIENCING Symptoms?: " << s[j].us_symptoms;
            cout << "\nWhat do you want to Edit?";
            cout << "\n\n\t\tEnter 1 to edit First Name\n";
            cout << "\t\tEnter 2 to edit Last Name\n";
            cout << "\t\tEnter 3 to edit Mobile No.\n";
            cout << "\t\tEnter 4 to edit Barangay\n";
            cout << "\t\tEnter 5 to edit City\n";
            cout << "\t\tEnter 6 to edit Temperature\n";
            cout << "\t\tEnter 7 to edit whether the user are EXPERIENCING ANY SYMPTOMS\n\n";
            cout << "\t\t------>";
            cin >> ch;
            cout << endl;
            switch (ch) {
            case 1:
                cout << "First Name: ";
                cin >> s[j].us_firstname;
                break;
            case 2:
                cout << "Last Name: ";
                cin >> s[j].us_lastname;
                break;
            case 3:
                cout << "Mobile No.: ";
                cin >> s[j].us_MobileNo;
                break;
            case 4:
                cout << "Barangay: ";
                cin >> s[j].us_barangay;
                break;
            case 5:
                cout << "City: ";
                cin >> s[j].us_city;
                break;
            case 6:
                cout << "Temperature: ";
                cin >> s[j].us_temp;
                break;
            case 7:
                cout << "EXPERIENCING ANY SYMTOMS? : ";
                cin >> s[j].us_symptoms;
                break;
            }
            break;
        }
    }
    if (j == i) {
        cout << "\n Error NOT FOUND\n";
        return;
    }
    fp.close();
    fstream fd;
    fd.open(UserInfo, ios::out | ios::trunc);
    if (!fd) {
        cout << "\nFile Not Found\n";
        exit(0);
    }
    for (j = 0; j < i; j++)
        us_pack(s[j]);
    fd.close();
}


int main() {
    cout << endl << endl << endl;
    cout << "\t\t\t\tWELCOME TO CONTACT TRACING SYSTEM\n\n";
    cout << "\t\t\t\t\tTRACE WITH US!!\n\n";
    cout << "\t\t\t\t    PRESS ENTER TO CONTINUE....\n\n";
    if (cin.get() == '\n') {
        system("cls");
        int choice, ch1, ch2;
        Information obj;
        cout << " Who are You?\n";
        cout << "<1> USER\n";
        cout << "<2> ADMIN\n";
        cout << "<3> EXIT\n";
        cout << "\nEnter Your Option: ";
        cin >> choice;
        switch (choice) {
        case 1:
            system("cls");
            cout << "WELCOME USER!\n";
            cout << "\nEnter your option\n";
            cout << "<1> Add Information\n";
            cout << "<2> View Information\n";
            cout << "<3> Go Back to Main Menu\n";
            cout << "<4> Exit\n";
            while (1) {
                cout << "\nENTER YOUR CHOICE: ";
                cin >> ch1;
                switch (ch1) {
                case 1:
                    cout << "\n-----------------------------------";
                    cout << "\n\tTrace With Us!\n";
                    cout << "-----------------------------------\n";
                    obj.us_add_data();
                    break;
                case 2:
                    obj.us_view();
                    break;
                case 3:
                    main();
                    break;
                case 4:
                    cout << "\n\n\tThank You for Tracing With Us!!\n";
                    _getch();
                    exit(0);
                    break;
                default:
                    cout << "\nInvalid Input\n\n";
                    system("pause");
                    break;
                }
            }
        case 2:
            system("cls");
            cout << "WELCOME ADMIN!\n";
            cout << "\nEnter your option:\n";
            cout << "<1> Add Information\n";
            cout << "<2> View Information\n";
            cout << "<3> Search Information\n";
            cout << "<4> Edit Information\n";
            cout << "<5> Go Back to Main Menu\n";
            cout << "<6> EXIT\n";
            while (1) {
                cout << "\nENTER YOUR CHOICE: ";
                cin >> ch2;
                switch (ch2)
                {
                case 1:
                    obj.us_add_data();
                    break;
                case 2:
                    obj.us_view();
                    break;
                case 3:
                    obj.ad_search();
                    break;
                case 4:
                    obj.ad_edit();
                    break;
                case 5:
                    main();
                    break;
                case 6:
                    cout << "\n\n\tThank You for Tracing With Us!!\n";
                    _getch();
                    exit(0);
                default:
                    cout << "\nInvalid Input\n\n";
                    system("pause");
                    break;
                }
            }
        case 3:
            cout << "\n\n\tThank You for Tracing With Us!!\n";
            _getch();
            exit(0);
            break;
        default:
            cout << "\nInvalid Input\n\n";
            system("pause");
            main();
            break;
        }
    }
}