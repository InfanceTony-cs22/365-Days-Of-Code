#include<iostream>

using namespace std;

int main()  {
    int num;
    cin >> num;
    
    char grade;
    
    if(num >= 90){
        grade = 'A';
    }
    else if(num >= 80){
        grade = 'B';
    }
    else if(num >= 70){
        grade = 'C';
    }
    else if(num >= 60){
        grade = 'D';
    }
    else if(num >= 50){
        grade = 'E';
    }
    else{
        grade = 'F';
    }
    
    cout << grade << endl;
    
    return 0;
}
