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

(defmacro while (test &body body)
  "While, like in most other languages."
  `(do ()
       ((not ,test))
     ,@body))

(defparameter *ldap* (make-8b-ldap))
(defparameter *anon-ldap* (make-8b-ldap :user "" :pass ""))

(defmacro with-ldap (ldap &body body)
  "Execute BODY in the context of LDAP bound to the ldap server."
  `(prog2
       (ldap:bind ,ldap)
       (progn ,@body)
     (ldap:unbind ,ldap)))

(defun strip-newlines (string &optional (replace-char nil))
  "Given a string, remove all newlines.

This is very irc specific where lines need to be all on one line.

Note that the newline is not replaced by a space!"
  (coerce
   (loop for char in (coerce string 'list)
      when (and replace-char (eq char #\Newline)) collect replace-char
      unless (eq char #\Newline) collect char)
   'string))

(defun print-single-entry (search-string &key (ldap *anon-ldap*)
                           attrs)
  (strip-newlines
   (ldap:ldif
    (with-ldap ldap
      (ldap:search ldap search-string
                   :attributes attrs)
      (ldap:next-search-result ldap)))
   #\ ))


(defun list-search-results (search-string &optional (ldap *anon-ldap*))
  "List of entries from a search."
  (with-ldap ldap
    (ldap:search ldap search-string))
  (let (result)
    (while (ldap:results-pending-p ldap)
      (push (ldap:next-search-result ldap) result))
    (nreverse (cdr result))))