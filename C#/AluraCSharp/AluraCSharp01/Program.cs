using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Variables vars = new Variables();

            Console.WriteLine("Integer:" + vars.getInteger() +
                ", Double: " + vars.getDoublePrecisionFloatingPoint());

            Console.WriteLine("Attempting to round-trip a Double with 'R':");
            double initialValue = 0.6822871999174;
            string valueString = initialValue.ToString("R");
            double roundTripped = double.Parse(valueString);
            Console.WriteLine("{0:R} = {1:R}: {2}\n",
                              initialValue, roundTripped, initialValue.Equals(roundTripped));

            Console.WriteLine("Attempting to round-trip a Double with 'G17':");
            string valueString17 = initialValue.ToString("G17");
            double roundTripped17 = double.Parse(valueString17);
            Console.WriteLine("{0:R} = {1:R}: {2}\n",
                              initialValue, roundTripped17, initialValue.Equals(roundTripped17));
        }
    }

    class Variables
    {
        int integer = 10;
        double doublePrecisionFloatingPoint = 3.1415;

        public int getInteger()
        {
            return this.integer;
        }

        public double getDoublePrecisionFloatingPoint()
        {
            return this.doublePrecisionFloatingPoint;
        }
    }

}
