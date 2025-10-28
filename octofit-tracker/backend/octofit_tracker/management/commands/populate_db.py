from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Create users
        user1 = User.objects.create_user(username='alice', email='alice@example.com', password='password')
        user2 = User.objects.create_user(username='bob', email='bob@example.com', password='password')
        user3 = User.objects.create_user(username='carol', email='carol@example.com', password='password')

        # チーム作成
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.set([user1, user2])
        team2.members.set([user3])

        # アクティビティ作成
        Activity.objects.create(user=user1, activity_type='run', duration=30, calories=250, date=timezone.now().date(), team=team1)
        Activity.objects.create(user=user2, activity_type='walk', duration=60, calories=200, date=timezone.now().date(), team=team1)
        Activity.objects.create(user=user3, activity_type='cycle', duration=45, calories=300, date=timezone.now().date(), team=team2)

        # リーダーボード作成
        Leaderboard.objects.create(team=team1, total_points=450)
        Leaderboard.objects.create(team=team2, total_points=300)

        # ワークアウト作成
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout2 = Workout.objects.create(name='Squats', description='Do 30 squats')
        workout1.suggested_for.set([user1, user3])
        workout2.suggested_for.set([user2])

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
