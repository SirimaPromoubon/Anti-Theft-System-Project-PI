       <?php
         if(isset($_GET['on'])){
                 // $gpio_on = shell_exec("/usr/local/bin/gpio -g write 7 1");
                exec("service motion start");
                console.log("OK");
                 echo "Project is on";
                 }
                 else if(isset($_GET['off'])){
                         // $gpio_off = shell_exec("/usr/local/bin/gpio -g write 7 0");
                   exec("service motion stop");
                         echo "Project is off";
                         console.log("Fail");
                         }
                         ?>
   