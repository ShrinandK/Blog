void displayValues(int* startPointer,int* counterVal) 
{     int tempVal = *counterVal;     
for(int iCount = 0;iCount < tempVal;iCount++)         
{             printf("\n%d", *(startPointer + iCount));         
} 
} 

void getPrimeNumber(int high,int low,int* counter) 
{     int i, flag, tempAdd;     
int* arrayStartAddr;     
int memNeed = (int)(0.5 * high);     
arrayStartAddr = malloc(memNeed * sizeof(int));     
if(arrayStartAddr == NULL)     
{         
printf("Error! memory not allocated.");         
exit(0);     
}      

while (low < high)     
{       flag = 0;       
// ignore numbers less than 2       
if (low <= 1) 
{          ++low;          
continue;       
}             
for (i = 2; i <= low / 2; ++i) 
{          
if (low % i == 0) 
{             
flag = 1;             
break;          
}       
}       
if (flag == 0)       
{           //printf("\n %d", low);          
*(arrayStartAddr + *counter) = low;          
tempAdd = *counter + 1;          
*counter = tempAdd;       
}           
++low;    
}    
displayValues(arrayStartAddr,counter);    
free(arrayStartAddr); 
}