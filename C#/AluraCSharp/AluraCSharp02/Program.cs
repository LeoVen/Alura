using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp02
{
    class Program
    {
        static void Main(string[] args)
        {
            MyClass myClass0 = new MyClass();

            myClass0.name = "MyClass0";
            myClass0.age = 10;
            myClass0.money = 100.0;

            MyClass myClass1 = new MyClass();

            myClass1.name = "MyClass1";
            myClass1.age = 10;
            myClass1.money = 100.0;

            Console.WriteLine(myClass0 == myClass1);
            Console.WriteLine(myClass0.Equals(myClass1));

            myClass0.Represent();
            myClass1.Represent();

            Console.ReadLine();
        }
    }
}
