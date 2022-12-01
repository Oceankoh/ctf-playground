<?php

class User{
    public $username = "administrator";
    public $access_token=0;
}

echo serialize(new User);
