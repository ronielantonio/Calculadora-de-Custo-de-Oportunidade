import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparativo Financeiro Profissional</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #0077B6;
            --secondary-color: #6c757d;
            --accent-color: #F1C40F;
            --success-color: #2ECC71;
            --danger-color: #E74C3C;
            --bg-start: #E0E0E0;
            --bg-end: #F0F0F0;
            --text-dark: #2c3e50;
            --text-light: #ffffff;
            --card-bg: #FFFFFF;
        }

        body {
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, var(--bg-start) 0%, var(--bg-end) 100%);
            color: var(--text-dark);
        }

        .container {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            max-width: 950px;
            width: 100%;
            margin: 20px;
        }

        h1 {
            color: var(--primary-color);
            text-align: center;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        p.subtitle {
            text-align: center;
            color: var(--secondary-color);
            margin-bottom: 2rem;
        }

        .tab-buttons {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .tab-btn {
            background-color: #eceff1;
            border: none;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 5px;
            border-radius: 10px;
        }

        .tab-btn:hover {
            background-color: #cfd8dc;
            transform: translateY(-2px);
        }

        .tab-btn.active {
            background-color: var(--primary-color);
            color: var(--text-light);
            box-shadow: 0 4px 15px rgba(0, 119, 182, 0.3);
            transform: translateY(-2px);
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.5s ease-in-out;
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--text-dark);
        }

        .form-group input {
            width: calc(100% - 22px);
            padding: 12px;
            border: 1px solid #dcdfe6;
            border-radius: 10px;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .form-group input:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 8px rgba(0, 119, 182, 0.2);
        }

        .button-group {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            margin-top: 2rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 14px 28px;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            flex-grow: 1;
            min-width: 150px;
        }

        .btn-primary {
            background-color: var(--primary-color);
            color: var(--text-light);
        }

        .btn-primary:hover {
            background-color: #005f8e;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 119, 182, 0.3);
        }

        .btn-secondary {
            background-color: var(--secondary-color);
            color: var(--text-light);
        }

        .btn-secondary:hover {
            background-color: #5a6268;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(108, 117, 125, 0.2);
        }

        .summary, .cdi-card, .comparison-card, .explanation {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
            border: 1px solid #e9ecef;
        }

        .summary h3, .comparison-card h4 {
            font-weight: 600;
            margin-top: 0;
            color: var(--text-dark);
        }

        .summary p {
            font-size: 1.6rem;
            font-weight: 700;
            margin: 0.5rem 0;
        }
        
        .summary p.final-balance {
            color: var(--success-color);
        }
        
        .summary p.total-juros {
            color: var(--primary-color);
        }
        
        .summary p span, .comparison-card p span {
            display: block;
        }

        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-top: 1.5rem;
            overflow: hidden;
            border-radius: 10px;
        }

        table th, table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #e9ecef;
        }

        table th {
            background-color: var(--primary-color);
            color: var(--text-light);
            font-weight: 600;
            font-size: 0.95rem;
        }

        table tbody tr:nth-child(even) {
            background-color: #f8f9fa;
        }

        .explanation ul {
            text-align: left;
            padding-left: 20px;
        }

        .cdi-card {
            background-color: #ecf0f1;
            border: 1px solid #bdc3c7;
        }

        .cdi-card h4 {
            color: var(--secondary-color);
        }
        
        .cdi-card a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 600;
        }
        
        .comparison-card {
            background-color: #e8f6f3;
            border: 1px solid #a2d9ce;
        }
        
        .comparison-card .winner {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--success-color);
            margin-top: 1rem;
        }
        
        .comparison-card .loser {
            color: var(--danger-color);
        }
        
        .flex-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .flex-row input[type="checkbox"] {
            width: auto;
            transform: scale(1.2);
            margin: 0;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 1.5rem;
            }
            h1 {
                font-size: 1.8rem;
            }
            .tab-btn {
                font-size: 0.9rem;
                padding: 10px 15px;
            }
            .btn {
                width: 100%;
                min-width: unset;
            }
            .button-group {
                flex-direction: column;
            }
            table th, table td {
                padding: 10px;
                font-size: 0.8rem;
            }
            .summary p {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Comparativo Financeiro</h1>
        <p class="subtitle">Análise de Juros com Opção de Saques Mensais e Custo de Oportunidade</p>

        <div class="tab-buttons">
            <button class="tab-btn active" onclick="showTab('tab-saques', this)">Juros com Saques</button>
            <button class="tab-btn" onclick="showTab('tab-oportunidade', this)">Custo de Oportunidade</button>
            <button class="tab-btn" onclick="showTab('tab-explanation', this)">Explicação</button>
        </div>

        <div id="tab-saques" class="tab-content active">
            <div class="cdi-card">
                <h4>Taxa de Juros de Referência (CDI)</h4>
                <p>Para obter o valor atual do CDI, consulte a taxa SELIC no site oficial do Banco Central. O CDI geralmente acompanha a SELIC de perto.</p>
                <a href="https://www.bcb.gov.br/" target="_blank">Consultar no site do Banco Central</a>
            </div>
            
            <form id="saques-form">
                <div class="form-group">
                    <label for="initial-principal-saques">Capital Inicial (R$)</label>
                    <input type="number" id="initial-principal-saques" value="3000" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="monthly-withdrawal-saques">Retirada Mensal (R$)</label>
                    <input type="number" id="monthly-withdrawal-saques" value="300" step="0.01" required>
                </div>
                
                <div class="form-group">
                    <div class="flex-row">
                        <label for="monthly-rate-saques">Taxa Mensal (%)</label>
                        <input type="checkbox" id="use-cdi-saques" onclick="toggleCdiRate('saques')">
                        <label for="use-cdi-saques" style="font-weight: normal; margin-left: 5px;">Usar 100% do CDI</label>
                    </div>
                    <input type="number" id="monthly-rate-saques" value="1" step="0.01" required>
                </div>
                
                <div class="form-group" id="cdi-rate-group-saques" style="display: none;">
                    <label for="cdi-annual-rate-saques">Taxa Anual do CDI (%)</label>
                    <input type="number" id="cdi-annual-rate-saques" value="10" step="0.01" required>
                </div>
                
                <div class="form-group">
                    <label for="num-months-saques">Número de Meses</label>
                    <input type="number" id="num-months-saques" value="10" required>
                </div>
                <div class="button-group">
                    <button type="button" class="btn btn-primary" onclick="calcularJuros()">Calcular Juros</button>
                    <button type="button" class="btn btn-secondary" onclick="limpar('saques-form')">Limpar</button>
                </div>
            </form>

            <div id="results-saques" style="display: none;">
                <div class="summary">
                    <h3>Resumo Final</h3>
                    <p class="final-balance">Saldo Final: <span id="final-balance-saques"></span></p>
                    <p class="total-juros">Juros Totais Acumulados: <span id="total-juros-saques"></span></p>
                </div>

                <h3>Log Detalhado Mês a Mês</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Mês</th>
                            <th>Saldo Inicial</th>
                            <th>Juros</th>
                            <th>Saldo Final</th>
                        </tr>
                    </thead>
                    <tbody id="monthly-log-body-saques">
                        </tbody>
                </table>
            </div>
        </div>

        <div id="tab-oportunidade" class="tab-content">
            <div class="cdi-card">
                <h4>Taxa de Juros de Referência (CDI)</h4>
                <p>Para obter o valor atual do CDI, consulte a taxa SELIC no site oficial do Banco Central. O CDI geralmente acompanha a SELIC de perto.</p>
                <a href="https://www.bcb.gov.br/" target="_blank">Consultar no site do Banco Central</a>
            </div>

            <form id="oportunidade-form">
                <div class="form-group">
                    <label for="initial-principal-oportunidade">Valor do Produto (R$)</label>
                    <input type="number" id="initial-principal-oportunidade" value="3000" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="monthly-withdrawal-oportunidade">Valor da Parcela (R$)</label>
                    <input type="number" id="monthly-withdrawal-oportunidade" value="300" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="discount-rate-oportunidade">Desconto à Vista (%)</label>
                    <input type="number" id="discount-rate-oportunidade" value="0" step="0.01" required>
                </div>
                <div class="form-group">
                    <div class="flex-row">
                        <label for="monthly-rate-oportunidade">Taxa Mensal (%)</label>
                        <input type="checkbox" id="use-cdi-oportunidade" onclick="toggleCdiRate('oportunidade')">
                        <label for="use-cdi-oportunidade" style="font-weight: normal; margin-left: 5px;">Usar 100% do CDI</label>
                    </div>
                    <input type="number" id="monthly-rate-oportunidade" value="1" step="0.01" required>
                </div>
                <div class="form-group" id="cdi-rate-group-oportunidade" style="display: none;">
                    <label for="cdi-annual-rate-oportunidade">Taxa Anual do CDI (%)</label>
                    <input type="number" id="cdi-annual-rate-oportunidade" value="10" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="num-months-oportunidade">Número de Meses</label>
                    <input type="number" id="num-months-oportunidade" value="10" required>
                </div>
                <div class="button-group">
                    <button type="button" class="btn btn-primary" onclick="analisarOportunidade()">Analisar Oportunidade</button>
                    <button type="button" class="btn btn-secondary" onclick="limpar('oportunidade-form')">Limpar</button>
                </div>
            </form>

            <div id="results-oportunidade" style="display: none;">
                <div class="comparison-card">
                    <h4>Análise Comparativa Final</h4>
                    <p>Ganho Total (Compra Parcelada): <span id="final-gain-parcelado"></span></p>
                    <p>Ganho Total (Compra à Vista): <span id="final-gain-vista"></span></p>
                    <p id="winner-message"></p>
                </div>

                <div class="chart-container">
                    <h3>Evolução dos Ganhos Acumulados</h3>
                    <canvas id="myChart"></canvas>
                </div>
            </div>
        </div>

        <div id="tab-explanation" class="tab-content">
            <div class="explanation">
                <h3>O Conceito: Custo de Oportunidade e Ganhos</h3>
                <p>Esta ferramenta vai além de um simples cálculo de juros. Ela ajuda a visualizar o **custo de oportunidade** de uma compra, ou seja, o que o seu dinheiro poderia estar rendendo se você fizesse uma escolha diferente. A análise se baseia nos **ganhos financeiros líquidos** de dois cenários:</p>
                <ul>
                    <li>**Ganho ao Parcelar:** O total de juros que você acumula no seu investimento inicial, mesmo que você use parte dele para pagar as parcelas do produto.</li>
                    <li>**Ganho ao Comprar à Vista:** O valor do desconto que você recebeu, somado aos juros que esse valor renderia se fosse investido.</li>
                </ul>

                <h4>Como Usar as Abas</h4>
                <ul>
                    <li>
                        <strong>Aba "Juros com Saques":</strong> Use esta aba para simular a evolução do seu dinheiro em um investimento, considerando retiradas mensais para o pagamento de contas ou parcelas. O resultado é o saldo final e os juros totais acumulados.
                    </li>
                    <li>
                        <strong>Aba "Custo de Oportunidade":</strong> Use esta aba para comparar diretamente as duas opções de compra (parcelada vs. à vista com desconto). O gráfico de **Evolução dos Ganhos Acumulados** mostra o crescimento financeiro em cada cenário. A linha que estiver **mais alta** no final é a que representa a decisão financeiramente mais vantajosa.
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        let myChartInstance = null;
        // Obtenha as variáveis CSS
        const style = getComputedStyle(document.body);
        const primaryColor = style.getPropertyValue('--primary-color');
        const successColor = style.getPropertyValue('--success-color');
        const textDark = style.getPropertyValue('--text-dark');
        const gridColor = style.getPropertyValue('--bg-start');

        function formatarMoeda(valor) {
            return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
        }

        function showTab(tabId, element) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));

            document.getElementById(tabId).classList.add('active');
            element.classList.add('active');
        }

        function toggleCdiRate(tab) {
            const useCdiCheckbox = document.getElementById(`use-cdi-${tab}`);
            const monthlyRateInput = document.getElementById(`monthly-rate-${tab}`);
            const cdiRateGroup = document.getElementById(`cdi-rate-group-${tab}`);

            if (useCdiCheckbox.checked) {
                monthlyRateInput.disabled = true;
                monthlyRateInput.style.display = 'none';
                cdiRateGroup.style.display = 'block';
            } else {
                monthlyRateInput.disabled = false;
                monthlyRateInput.style.display = 'block';
                cdiRateGroup.style.display = 'none';
            }
        }

        function calcularJuros() {
            const initialPrincipal = parseFloat(document.getElementById('initial-principal-saques').value);
            const monthlyWithdrawal = parseFloat(document.getElementById('monthly-withdrawal-saques').value);
            let monthlyRate;
            const useCdi = document.getElementById('use-cdi-saques').checked;
            
            if (useCdi) {
                const cdiAnnualRate = parseFloat(document.getElementById('cdi-annual-rate-saques').value);
                if (isNaN(cdiAnnualRate)) {
                    alert("Por favor, insira um valor válido para a Taxa Anual do CDI.");
                    return;
                }
                monthlyRate = Math.pow(1 + (cdiAnnualRate / 100), 1/12) - 1;
            } else {
                monthlyRate = parseFloat(document.getElementById('monthly-rate-saques').value) / 100;
            }
            
            const numMonths = parseInt(document.getElementById('num-months-saques').value);

            if (isNaN(initialPrincipal) || isNaN(monthlyWithdrawal) || isNaN(monthlyRate) || isNaN(numMonths) || numMonths <= 0) {
                alert("Por favor, preencha todos os campos com valores válidos.");
                return;
            }

            let currentBalance = initialPrincipal;
            let totalInterest = 0;
            const logData = [];

            for (let mes = 1; mes <= numMonths; mes++) {
                const interestEarned = currentBalance * monthlyRate;
                totalInterest += interestEarned;
                currentBalance += interestEarned;
                currentBalance -= monthlyWithdrawal;
                
                logData.push({
                    month: mes,
                    initialBalance: currentBalance + monthlyWithdrawal - interestEarned,
                    interest: interestEarned,
                    finalBalance: currentBalance
                });
            }
            const finalBalance = currentBalance;

            document.getElementById('final-balance-saques').textContent = formatarMoeda(finalBalance);
            document.getElementById('total-juros-saques').textContent = formatarMoeda(totalInterest);

            const tableBody = document.getElementById('monthly-log-body-saques');
            tableBody.innerHTML = '';

            logData.forEach(data => {
                const row = tableBody.insertRow();
                row.insertCell(0).textContent = data.month;
                row.insertCell(1).textContent = formatarMoeda(data.initialBalance);
                row.insertCell(2).textContent = formatarMoeda(data.interest);
                row.insertCell(3).textContent = formatarMoeda(data.finalBalance);
            });
            
            document.getElementById('results-saques').style.display = 'block';
        }

        function analisarOportunidade() {
            const initialPrincipal = parseFloat(document.getElementById('initial-principal-oportunidade').value);
            const monthlyWithdrawal = parseFloat(document.getElementById('monthly-withdrawal-oportunidade').value);
            const discountRate = parseFloat(document.getElementById('discount-rate-oportunidade').value) / 100;
            let monthlyRate;
            const useCdi = document.getElementById('use-cdi-oportunidade').checked;
            
            if (useCdi) {
                const cdiAnnualRate = parseFloat(document.getElementById('cdi-annual-rate-oportunidade').value);
                if (isNaN(cdiAnnualRate)) {
                    alert("Por favor, insira um valor válido para a Taxa Anual do CDI.");
                    return;
                }
                monthlyRate = Math.pow(1 + (cdiAnnualRate / 100), 1/12) - 1;
            } else {
                monthlyRate = parseFloat(document.getElementById('monthly-rate-oportunidade').value) / 100;
            }
            
            const numMonths = parseInt(document.getElementById('num-months-oportunidade').value);

            if (isNaN(initialPrincipal) || isNaN(monthlyWithdrawal) || isNaN(monthlyRate) || isNaN(numMonths) || numMonths <= 0) {
                alert("Por favor, preencha todos os campos com valores válidos.");
                return;
            }

            let currentBalance = initialPrincipal;
            let totalInterestParcelado = 0;
            const chartLabels = ["Início"];
            const chartGanhosParcelado = [0];

            for (let mes = 1; mes <= numMonths; mes++) {
                const interestEarned = currentBalance * monthlyRate;
                totalInterestParcelado += interestEarned;
                currentBalance += interestEarned;
                currentBalance -= monthlyWithdrawal;
                chartLabels.push(`Mês ${mes}`);
                chartGanhosParcelado.push(totalInterestParcelado);
            }

            const discountedValue = initialPrincipal * discountRate;
            let currentGainVista = discountedValue;
            const chartGanhosVista = [0];

            chartGanhosVista.push(discountedValue);

            for (let mes = 1; mes <= numMonths; mes++) {
                currentGainVista = currentGainVista * (1 + monthlyRate);
                chartGanhosVista.push(currentGainVista);
            }
            
            if (myChartInstance) {
                myChartInstance.destroy();
            }

            const ctx = document.getElementById('myChart').getContext('2d');
            myChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: chartLabels,
                    datasets: [
                        {
                            label: 'Ganhos Acumulados - Opção Parcelada',
                            data: chartGanhosParcelado,
                            borderColor: primaryColor,
                            backgroundColor: 'rgba(0, 119, 182, 0.1)',
                            borderWidth: 2,
                            pointBackgroundColor: primaryColor,
                            tension: 0.3
                        },
                        {
                            label: 'Ganhos Acumulados - Opção à Vista (com desconto)',
                            data: chartGanhosVista,
                            borderColor: successColor,
                            backgroundColor: 'rgba(46, 204, 113, 0.1)',
                            borderWidth: 2,
                            pointBackgroundColor: successColor,
                            tension: 0.3
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Ganhos Acumulados (R$)',
                                color: textDark
                            },
                            grid: {
                                color: gridColor
                            },
                            ticks: {
                                callback: function(value, index, values) {
                                    return formatarMoeda(value);
                                }
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Mês',
                                color: textDark
                            },
                            grid: {
                                color: gridColor
                            }
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    label += formatarMoeda(context.parsed.y);
                                    return label;
                                }
                            }
                        }
                    }
                }
            });

            document.getElementById('final-gain-parcelado').textContent = formatarMoeda(totalInterestParcelado);
            document.getElementById('final-gain-vista').textContent = formatarMoeda(currentGainVista);

            const winnerMessage = document.getElementById('winner-message');
            if (totalInterestParcelado > currentGainVista) {
                winnerMessage.textContent = "A opção parcelada é mais vantajosa! ✨";
                winnerMessage.className = "winner";
            } else if (currentGainVista > totalInterestParcelado) {
                winnerMessage.textContent = "A opção à vista é mais vantajosa! 🎉";
                winnerMessage.className = "winner";
            } else {
                winnerMessage.textContent = "Ambas as opções têm o mesmo resultado final.";
                winnerMessage.className = "";
            }
            
            document.getElementById('results-oportunidade').style.display = 'block';
        }

        function limpar(formId) {
            document.getElementById(formId).reset();
            const resultsId = formId === 'saques-form' ? 'results-saques' : 'results-oportunidade';
            document.getElementById(resultsId).style.display = 'none';

            if (myChartInstance) {
                myChartInstance.destroy();
            }

            toggleCdiRate(formId === 'saques-form' ? 'saques' : 'oportunidade');
        }

        document.addEventListener('DOMContentLoaded', () => {
            toggleCdiRate('saques');
            toggleCdiRate('oportunidade');
        });
    </script>
</body>
</html>
"""

st.set_page_config(layout="wide")
st.components.v1.html(html_code, height=1000, scrolling=True)
