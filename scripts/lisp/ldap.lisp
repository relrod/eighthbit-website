(require :trivial-ldap)

(defpackage #:8b-ldap
  (:use :cl))

(in-package :8b-ldap)

;;; For eighthbit we use ssh tunnels to LDAP, so make sure this matches
;;; up with your local machine name. This may _not_ be localhost!
(defvar *default-host* "localhsot"
  "Location of ldap.")

(defvar *default-port* (the integer 2242)
  "Where to look for ldap.

This is not the default LDAP port, but we default to 2242 for ssh
tunnels to LDAP.")

(defvar *user* ""
  "User to interact with LDAP as.

Defaults to an empty string which means we are anonymous.")

(defvar *pass* ""
  "Password to auth to LDAP with.

Defautls to an empty string which means no pass.")

(defvar *root-base* "dc=eighthbit,dc=net"
  "All 8b LDAP things are under this base.")

;;; Load an optional config file, the lack of this should not cause this
;;; program to become unusable.
(load "config.lisp" :if-does-not-exist nil)

(defun make-8b-ldap (&key (user *user*) (pass *pass*)
                     (base *root-base*))
  "Make an ldap object for 8b's ldap."
  (ldap:new-ldap :host *default-host*
                 :port *default-port*
                 :user user
                 :pass pass
                 :base base))

(defparameter *ldap* (make-8b-ldap))

