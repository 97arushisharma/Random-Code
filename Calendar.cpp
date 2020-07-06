#include<iostream.h>
#include<conio.h>
#include<math.h>
#include<stdio.h>
int d[3];
int tn[12]={0,3,3,6,1,4,6,2,5,0,3,5};
int tl[2]={6,2};

char *days[]={"SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"};
int cent[]={6,4,2,0};

void calcu(int d[]);

void input()
{
	cout<<"ENTER THE DATE YOU WANT TO FIND (dd mm yyyy)\n\n";
	for(int i=0;i<3;i++)
	{
		cin>>d[i];
		cout<<"\n";
	}
	calcu(d);
}

void main()                                                          //Main function
{
	clrscr();
	char ch='y';
	while(ch=='y')
	{
		input();
		cout<<"\nWANT TO SEE MORE?(y/n)\n";   
		cin>>ch;
	}
	getch();
}

void calcu(int d[])                                                      //Function to calculate
{       
  int sum;
	int d1=d[0];
	int m=d[1];
	int yr=d[2];
	int yrem=((yr%100)%4);
	int yrq=((yr%100)/4);
	int centrem=((yr/100)%4);
	if(m==01 || m==02)
	{	if((yr%100)==0||yrem==0)
		{
			if((yr%100)==0 && centrem!=0)
			{
				sum=d1+tn[m-1]+yrq+(yr%100)+cent[centrem];
			}
			else
				sum=d1+tl[m-1]+yrq+(yr%100)+cent[centrem];
		}
		else
		{
			sum=d1+tn[m-1]+yrq+(yr%100)+cent[centrem];
		}
	}
	else
	{
		sum=d1+tn[m-1]+yrq+(yr%100)+cent[centrem];
	}
	int j=0;
	j=(sum%7);
	puts(days[j]);
}
