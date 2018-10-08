using System;

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

            Vector v0 = new Vector(-2.0, 4.3, -3.14);
            Vector v1 = new Vector(5.3, -2.2, 3.0);
            Vector v2 = new Vector(1.1, -8.3, 0.8);

            Console.WriteLine(v0 + v1);
            Console.WriteLine(v0 - v1);
            Console.WriteLine(v0 + v1 - v2);

            Console.WriteLine(Vector.Total);

            Console.ReadLine();
        }
    }
}
