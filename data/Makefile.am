@INTLTOOL_DESKTOP_RULE@
@INTLTOOL_POLICY_RULE@

desktopdir       = $(datadir)/applications
desktop_in_files = wildbob.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

polkit_policydir = $(datadir)/polkit-1/actions
dist_polkit_policy_in_files = com.ubuntu.pkexec.wildbob.policy.in
dist_polkit_policy_DATA = $(dist_polkit_policy_in_files:.policy.in=.policy)

EXTRA_DIST = $(desktop_in_files) \
		$(desktop_DATA) \
		$(dist_polkit_policy_in_files)
