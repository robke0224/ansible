#!/bin/sh
if [ "$#" -gt 0 ]; then
	exec "$@"
fi

echo "Ansible controller container started. To run playbooks:"
echo "  docker compose run --rm ansible ansible-playbook /workspace/ansible/remove_profanity.yml -i /workspace/ansible/inventory.ini"
sleep infinity
