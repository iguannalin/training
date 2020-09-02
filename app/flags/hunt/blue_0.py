from plugins.training.app.base_flag import BaseFlag


name = "Initialize Hunt Badge"
challenge = 'This flag tests the environment to ensure the rest of the Hunt badge works correctly. This flag will ' \
            'pass only if the Gameboard plugin is enabled in Caldera.'
extra_info = """"""

operation_name = 'hunt_initialize'
adversary_id = 'b2d8e29a-fb11-4ba7-bde4-60d9a628784e'
agent_group = 'cert-win'


async def verify(services):
    return await BaseFlag.standard_verify_with_operation(services, operation_name, adversary_id, agent_group,
                                                         is_flag_satisfied)


async def is_flag_satisfied(services):
    return gameboard_available(services)


def gameboard_available(services):
    return 'gameboard_svc' in services
