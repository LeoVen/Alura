using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp03.Carros
{
    class Pickup : Veiculo
    {
        public override double Price { get; protected set; }
        public override uint GasTankSize { get; protected set; }
        public override string Name { get; protected set; }
        public override Engine Engine { get; protected set; }

        public Pickup(string name, double price, uint tankSize, string engineName, uint engineCylinders, double engineSize)
        {
            this.Price = price;
            this.GasTankSize = tankSize;
            this.Name = name;
            this.Engine = new Engine(engineName, engineCylinders, engineSize);
        }

        public override double GetPriceInflation(uint year)
        {
            return this.Price * Math.Pow(1.01, (double)(year));
        }

        public override double GetRange()
        {
            return this.GasTankSize / this.Engine.FuelUsage();
        }
    }
}
