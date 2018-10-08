using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp03.Carros
{
    public abstract class Veiculo
    {
        public abstract double Price { get; protected set; }
        public abstract uint GasTankSize { get; protected set; }
        public abstract string Name { get; protected set; }
        public abstract Engine Engine { get; protected set; }

        public abstract double GetRange();
        public abstract double GetPriceInflation(uint year);
    }
}
