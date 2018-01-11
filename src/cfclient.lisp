(in-package :cfclient)

(defun cb (x)  
  (setq icarus:state*
        (list (list 'SELF 'ME 'X 1 'Y 1)
              (list 'obs 'front 'range (rangefront x))
              (list 'obs 'back 'range (rangeback x))
              (list 'obs 'right 'range (rangeright x))
              (list 'obs 'left 'range (rangeleft x))
	      ))
  (ros-info nil "~&State updated!~&~A" icarus:state*))

(defun preattend (&optional (n 1))
  (with-ros-node ("listener" :spin nil)
    (subscribe "chatter" 'oa
               #'cb)
    (icarus:grun 1)
    (dotimes (i (- n 1))
      (icarus:cont 1)
      (sleep 1)
      )
    ;; (sleep 10)
    ))
