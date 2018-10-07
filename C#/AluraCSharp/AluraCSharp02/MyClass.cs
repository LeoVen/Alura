using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp02
{
    class MyClass
    {
        public string name;
        public int age;
        public double money;

        public void Represent()
        {
            Console.WriteLine(name + " " + age + " has " + money + " in bank");
        }
    }
}
