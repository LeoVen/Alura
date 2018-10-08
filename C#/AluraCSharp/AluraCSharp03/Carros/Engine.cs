using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp03.Carros
{
    public class Engine
    {
        public string Name { get; set; }
        public uint Cylinders { get; set; }
        public double Size { get; set; }

        public Engine(string name, uint cylinders, double size)
        {
            this.Name = name;
            this.Cylinders = cylinders;
            this.Size = size;
        }

        public double FuelUsage()
        {
            return this.Size / (double)this.Cylinders;
        }
    }
}
