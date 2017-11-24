#include<stdio.h>
int main(){
    int h, m;
    scanf("%d%d", &h, &m);
    if(m!=00 && m!=15 && m!=30 && m!=45){
        if(m==01) printf("one ");
        if(m==02) printf("two ");
        if(m==03) printf("three ");
        if(m==04) printf("four ");
        if(m==05) printf("five ");
        if(m==06) printf("six ");
        if(m==07) printf("seven ");
        if(m==8) printf("eight ");
        if(m==9) printf("nine ");
        if(m==10) printf("ten ");
        if(m==11) printf("eleven ");
        if(m==12) printf("twelve ");
        if(m==13) printf("thirteen ");
        if(m==14) printf("fourteen ");
        if(m==16) printf("sixteen ");
        if(m==17) printf("seventeen ");
        if(m==18) printf("eighteen ");
        if(m==19) printf("nineteen ");
        if(m==20) printf("twenty ");
        if(m==21) printf("twenty one ");
        if(m==22) printf("twenty two ");
        if(m==23) printf("twenty three ");
        if(m==24) printf("twenty four ");
        if(m==25) printf("twenty five ");
        if(m==26) printf("twenty six ");
        if(m==27) printf("twenty seven ");
        if(m==28) printf("twenty eight ");
        if(m==29) printf("twenty nine ");
        if(m==59) printf("one ");
        if(m==58) printf("two ");
        if(m==57) printf("three ");
        if(m==56) printf("four ");
        if(m==55) printf("five ");
        if(m==54) printf("six ");
        if(m==53) printf("seven ");
        if(m==52) printf("eight ");
        if(m==51) printf("nine ");
        if(m==50) printf("ten ");
        if(m==49) printf("eleven ");
        if(m==48) printf("twelve ");
        if(m==47) printf("thirteen ");
        if(m==46) printf("fourteen ");
        if(m==44) printf("sixteen ");
        if(m==43) printf("seventeen ");
        if(m==42) printf("eighteen ");
        if(m==41) printf("nineteen ");
        if(m==40) printf("twenty ");
        if(m==39) printf("twenty one ");
        if(m==38) printf("twenty two ");
        if(m==37) printf("twenty three ");
        if(m==36) printf("twenty four ");
        if(m==35) printf("twenty five ");
        if(m==34) printf("twenty six ");
        if(m==33) printf("twenty seven ");
        if(m==32) printf("twenty eight ");
        if(m==31) printf("twenty nine ");
        if(m<30){
            if(m==1) printf("minute past ");
            else printf("minutes past ");
        }
        else{
            if(m==59) printf("minute to ");
            else printf("minutes to ");
        }
    }
    if(m==15) printf("quarter past ");
    if(m==30) printf("half past ");
    if(m==45) printf("quarter to ");
    if(m!=00 && m<=30){
        if(h==01) printf("one");
        if(h==02) printf("two");
        if(h==03) printf("three");
        if(h==04) printf("four");
        if(h==05) printf("five");
        if(h==06) printf("six");
        if(h==07) printf("seven");
        if(h==8) printf("eight");
        if(h==9) printf("nine");
        if(h==10) printf("ten");
        if(h==11) printf("eleven");
    }
    if(m!=00 && m>30){
        if(h==01) printf("two");
        if(h==02) printf("three");
        if(h==03) printf("four");
        if(h==04) printf("five");
        if(h==05) printf("six");
        if(h==06) printf("seven");
        if(h==7) printf("eight");
        if(h==8) printf("nine");
        if(h==9) printf("ten");
        if(h==10) printf("eleven");
        if(h==11) printf("twelve");
    }
    if(m==00){
        if(h==01) printf("one");
        if(h==02) printf("two");
        if(h==03) printf("three");
        if(h==04) printf("four");
        if(h==05) printf("five");
        if(h==06) printf("six");
        if(h==07) printf("seven");
        if(h==8) printf("eight");
        if(h==9) printf("nine");
        if(h==10) printf("ten");
        if(h==11) printf("eleven");
        printf(" o' clock");
    }
}
