(defsystem crazyflie-clients-lisp
  :depends-on (roslisp std_msgs-msg crazyflie_clients_python-msg crazyflie_clients_python-srv)
  :components
  ((:module "src"
    :components
    ((:file "cfclient"
      :depends-on ("package"))
     (:file "package"))))
  )
