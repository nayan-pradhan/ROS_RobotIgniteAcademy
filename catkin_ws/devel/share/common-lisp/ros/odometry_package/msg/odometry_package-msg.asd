
(cl:in-package :asdf)

(defsystem "odometry_package-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "odometry_msg" :depends-on ("_package_odometry_msg"))
    (:file "_package_odometry_msg" :depends-on ("_package"))
  ))