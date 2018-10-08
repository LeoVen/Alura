using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp03.Funcionarios
{
    class Coordenador : Diretor
    {
        public uint Projects { get; protected set; }

        public Coordenador(string nome, ulong cpf, double salario, double aumentoAnual, uint projects = 0)
            : base(nome, cpf, salario, aumentoAnual)
        {
            this.Projects = projects;
        }

        public override double GetBonificacao()
        {
            return 2 * base.GetBonificacao();
        }

        public override void AumentarSalario()
        {
            base.AumentarSalario();
        }
    }
}
