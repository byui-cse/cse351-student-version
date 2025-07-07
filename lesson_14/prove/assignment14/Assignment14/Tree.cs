using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Assignment14;

public class Tree
{
    private readonly Dictionary<long, Person> _people;
    private readonly Dictionary<long, Family> _families;
    private readonly long _startFamilyId;

    public int PersonCount => _people.Count;
    public int FamilyCount => _families.Count;

    public Tree(long startFamilyId)
    {
        _people = new Dictionary<long, Person>();
        _families = new Dictionary<long, Family>();
        _startFamilyId = startFamilyId;
    }

    public void AddPerson(Person person)
    {
        if (_people.ContainsKey(person.Id))
        {
            Console.WriteLine($"ERROR: Person with ID = {person.Id} already exists in the tree.");
        }
        else
        {
            _people[person.Id] = person;
        }
    }

    public void AddFamily(Family family)
    {
        if (_families.ContainsKey(family.Id))
        {
            Console.WriteLine($"ERROR: Family with ID = {family.Id} already exists in the tree.");
        }
        else
        {
            _families[family.Id] = family;
        }
    }

    public Person? GetPerson(long id)
    {
        _people.TryGetValue(id, out var person);
        return person;
    }

    public Family? GetFamily(long id)
    {
        _families.TryGetValue(id, out var family);
        return family;
    }

    public void Display()
    {
        Logger.Write("\n\n");
        string title = " TREE DISPLAY ";
        int padding = (40 - title.Length) / 2;
        Logger.Write(new string('*', padding) + title + new string('*', padding));

        foreach (var family in _families.Values)
        {
            Logger.Write($"Family id: {family.Id}");

            // Husband and Wife
            var husband = GetPerson(family.HusbandId);
            Logger.Write(husband != null
                ? $"  Husband: {husband.Name}, {husband.Birth}"
                : "  Husband: None");

            var wife = GetPerson(family.WifeId);
            Logger.Write(wife != null
                ? $"  Wife: {wife.Name}, {wife.Birth}"
                : "  Wife: None");

            // Parents of Husband
            DisplayParents("Husband", husband);

            // Parents of Wife
            DisplayParents("Wife", wife);

            // Children
            var childNames = family.Children
                .Select(childId => GetPerson(childId)?.Name)
                .Where(name => name != null);
            Logger.Write($"  Children: {string.Join(", ", childNames)}");
        }

        Logger.Write("");
        Logger.Write($"Number of people                    : {PersonCount}");
        Logger.Write($"Number of families                  : {FamilyCount}");
        Logger.Write($"Max generations                     : {CountGenerations()}");
        Logger.Write($"People connected to starting family : {CountConnectedToStart()}");
    }
    
    private void DisplayParents(string role, Person? person)
    {
        if (person == null)
        {
            Logger.Write($"  {role} Parents: None");
            return;
        }

        var parentFamily = GetFamily(person.ParentId);
        if (parentFamily != null)
        {
            var father = GetPerson(parentFamily.HusbandId);
            var mother = GetPerson(parentFamily.WifeId);
            if (father != null && mother != null)
            {
                Logger.Write($"  {role} Parents: {father.Name} and {mother.Name}");
                return;
            }
        }
        Logger.Write($"  {role} Parents: None");
    }

    private int CountConnectedToStart()
    {
        var indsSeen = new HashSet<long>();

        void RecursiveCount(long familyId)
        {
            if (!_families.ContainsKey(familyId)) return;

            var fam = _families[familyId];

            // Husband
            var husband = GetPerson(fam.HusbandId);
            if (husband != null)
            {
                if (indsSeen.Add(husband.Id)) // Add returns true if the item was new
                {
                    RecursiveCount(husband.ParentId);
                }
            }
            
            // Wife
            var wife = GetPerson(fam.WifeId);
            if (wife != null)
            {
                if (indsSeen.Add(wife.Id))
                {
                    RecursiveCount(wife.ParentId);
                }
            }

            // Children
            foreach (var childId in fam.Children)
            {
                indsSeen.Add(childId);
            }
        }

        RecursiveCount(_startFamilyId);
        return indsSeen.Count;
    }

    private int CountGenerations()
    {
        int maxGen = -1;

        void RecursiveGen(long familyId, int currentGen)
        {
            if (!_families.ContainsKey(familyId)) return;
            
            if (maxGen < currentGen)
            {
                maxGen = currentGen;
            }

            var fam = _families[familyId];

            var husband = GetPerson(fam.HusbandId);
            if (husband != null)
            {
                RecursiveGen(husband.ParentId, currentGen + 1);
            }

            var wife = GetPerson(fam.WifeId);
            if (wife != null)
            {
                RecursiveGen(wife.ParentId, currentGen + 1);
            }
        }

        RecursiveGen(_startFamilyId, 0);
        return maxGen + 1;
    }

    public bool PersonExists(long id)
    {
        return _people.ContainsKey(id);
    }
}