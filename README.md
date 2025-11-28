<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>EMIRATES</title>
</head>
<body background='самолет111.jpg' width="1%" marginheight="1%">
        <style>

           body {
                background: url('самолет111.jpg');
                background-size: cover;
                background-repeat: no-repeat;





                }
           img{
                width:1%}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    8
           .main {
                background-color:white;
                margin:auto ;
                margin-top:30px;
                width:980px;
                padding:20px;
                border:2px black solid;
                border-radius:15px;

                border: 10px solid rgba(80, 55, 80, 0.5);
                background: url('img/primer-fona.jpg');
                width: 130px;
                height: 116px;}
           input{
                width:35%;
                margin:10px;
                padding:15px 10px;
                fond-size:12px;
                border-radius:15px;
                background-color:pink





                }




           .trff{

                background-color:pink;
                border:1 px solid;
                padding:11px;
                margin-left: auto;
                margin-right: auto;
                width:30%;



               border: 10px solid rgba(80, 55, 80, 0.5);
               border-radius:25px;



            }
           .center{
                margin-top:30px;
                text-align:center;
                }
           button {

            padding: 11px 20px;
            border-radius: 1px;
            text-decoration: none;
            background-color:pink;
            color: white;
           }

           button:hover {
                background-color: orange
           }
         #form {

            display: none;
            text-align: center;

         }
         #tr {

            display: none;
            tr-align: center;

         }





        </style>


        <div class="trff">
            <p class="center">Emirates</p>
        </div>
        <div class="center">
                <button    id="buy">купить билет  </button>


        </div>

        <div >
        <form id="form">
            <input type="text" placeholder="Ваше имя">
            <input type="text" placeholder="Ваш номер телефона">
            <button    id="zd">оформить заказ  </button>
        </form>
        </div>







        <script src="https://telegram.org/js/telegram-web-app.js?59"></script>
        <script>

            let tg = window.Telegram.WebApp;
            let order = document.getElementById('order');
            let buy = document.getElementById('buy');

            tg.expand();


            buy.addEventListener('click', ()=> {
                    document.getElementById('buy').style.display = 'none';
                    document.getElementById('form').style.display = 'block';

            });

            order.addEventListener('click', ()=> {
                    document.getElementById('error').innerText='';
                    let name = document.getElementById('user_name').value;
                    let number = document.getElementById('user_number').value;

                    if(name.length < 2) {
                        document.getElementById('error').innerText = 'ошибка имени'
                        return;
                    }
                    if(number.length < 9) {
                        document.getElementById('error').innerText = 'ошибка номера'
                        return;
                    }


                    let data = {
                        name: name,
                        number: number
                      }

                    tg.sendData(JSON.stringify(data));

                    tg.close();
            });





        </script>



</body>
</html>
